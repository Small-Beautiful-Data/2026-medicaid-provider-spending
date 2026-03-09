# # 🪶 Featherweight Databases
#
# DuckDB is like SQLite, but for analytics.
#
# 0. Download Data Manually❓
# 1. Import Data
# 2. Create View
# 3. Confirm Everything Worked
# 4. Do Something Else
#
# This script creates a new file called `medicaid_provider_spending.duckdb` in the data folder. This is where DuckDB will store our data, the view, etc.
#
# ### Important notes:
#
# - To save time, I downloaded the data locally before we began and unzipped it.
# - This script uses logging to help us understand how quickly everything runs.
#

# +
# Init
import os
import zipfile
from pathlib import Path

import duckdb as db
from loguru import logger

logger.add("featherweight_analytics.log")
logger.info("---- Import ----")
# -

# # 0. Download Data Manually❓
#
# - This is the most complex part of today's discussion.
# - Someone at DOGE uploaded a zipped CSV file to Hugging Face.
# - This causes HuggingFace's own datasets library and tools such as DuckDB, which are compatible with HuggingFace's `hf://` URLs, to fail.
# - A simple parquet file likely would have been smaller.

# +
# Downloads & unzips Medicaid Provider Spending Data
# Skips the download if the file exists.
mps_zip_path = Path("./data/medicaid-provider-spending.csv.zip")
mps_csv_path = Path("./data/medicaid-provider-spending.csv")


# Do NOT use the HF datasets package or polars to download this directly because it will fail.
if mps_csv_path.exists():
    logger.info(f"Medicaid Provider Spending, {mps_zip_path}, already exists.")
else:
    logger.info("Downloading Medicaid Provider Spending")
    import httpx
    mps_url = "https://huggingface.co/datasets/HHS-Official/medicaid-provider-spending/resolve/main/medicaid-provider-spending.csv.zip?download=true"
    with httpx.stream("GET", mps_url, follow_redirects=True) as response:
        response.raise_for_status() # Raise an exception for 4xx/5xx responses
        with open(mps_zip_path, "wb") as f:
            for chunk in response.iter_bytes():
                f.write(chunk)
    with zipfile.ZipFile(mps_zip_path, 'r') as zip_ref:
        # Extract the specific file
        zip_ref.extract("medicaid-provider-spending.csv", "./data/")
    logger.success(f"All done, {mps_csv_path}, is ready to go.")
# -

# # 1. Import Data
#
# Our local data warehouse will consist of two datasets:
#
# - Medicaid Provider Spending Data (from local CSV): `medicaid_provider_spending`
# - HCPCS Codes (From parquet, directly from HuggingFace): `hcpcs_codes`
#
# This is likely the easiest database build you have ever seen.

# Connect to DuckDB database
# If it doesn't exist, this creates the file.
ddb_path = Path("./data/medicaid_provider_spending.duckdb")
con = db.connect(ddb_path)

# +
# Import data into our DuckDB tables.
# Five commands. Three of which are logging.

logger.info("Importing data into DuckDB.")

# Imports CSV data from our local file system.
con.execute(f"""
create or replace table medicaid_provider_spending as
    select *
    from read_csv('{mps_csv_path}')
    --where . . . 
""")
logger.success("Table medicaid_provider_spending created.")


# Imports parquet data directly from Hugging Face!
con.execute("""
create or replace table hcpcs_codes as
    select *
    from read_parquet("hf://datasets/atta00/cpt-hcpcs-codes/data/test-00000-of-00001.parquet")
""")
logger.success("Table hcpcs_codes created.")
# -

# # 2. Create View
#
# This view, `vw_medicaid_provider_spending`, joins the Medicaid Provider Spending data to the reference table of HCPCS codes, making the end result a more usable product.

# +
# Merge our two tables with a view.

# Creates a view for our analysis which adds some useful features
# and joins our two source tables.
con.execute("""
create or replace view vw_medicaid_provider_spending as
    select
         mp.billing_provider_npi_num
        ,mp.servicing_provider_npi_num
        ,mp.hcpcs_code
        ,hc.description hcpcs_desc
        ,hc.title hcpcs_group
        ,hc.category hcpcs_category
        ,hc.type code_type
        ,cast(concat(mp.claim_from_month, '-01') as date) claim_from_month
        ,extract('year' from cast(concat(mp.claim_from_month, '-01') as date)) claim_from_year
        ,mp.total_unique_beneficiaries
        ,mp.total_claims
        ,mp.total_paid
    from medicaid_provider_spending mp
    left join hcpcs_codes hc
    on mp.hcpcs_code = hc.code
""")
logger.success("Created view vw_medicaid_provider_spending")
# -


# # 3. Confirm Everything Worked
#
# Let's just look at our data and make sure it looks OK.
#
# - Limit your results, or load everything into RAM. Your choice.
# - We have columns from both tables.
# - Unfortunately, our capitalization is not consistent.
#     - That's fine in SQL, but can cause problems in Python.
#     - We will address that in `analysis.py`.

# Review vw_medicaid_provider_spending
# Don't forget to limit the result set!
con.sql("""
select *
from vw_medicaid_provider_spending
-- Limit the results, or load it all into RAM!
limit 100
""").pl()

# # 4. Do Something Else
#
# - Close our connections.
# - Wrap up our logging.
# - *Quick tour of the DuckDB CLI and GUI tools.*

# Have a nice day!
con.close()
logger.success("Successfully imported data into DuckDB. Have a nice day!")
