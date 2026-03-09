# # 🪶 Featherweight Datawarehouse
#
# 0. Upload
# 1. Share
# 2. Do Something Else

# +
import os
from pathlib import Path

import duckdb as db
from dotenv import load_dotenv
from loguru import logger

load_dotenv()

logger.add("featherweight_analytics.log")
logger.info("---- Upload ----")
# -

# # Upload
#
# 0. Upload
# 1. Share
#
# Comments:
#
# - This script is even shorter than `import.py`.
# - Had DOGE uploaded a CSV, Excel, or Parquet file to HuggingFace, downloading the data locally would not even have ever been necessary, except for demonstrative purposes.

# # 0. Upload
#
# - Bulk uploads EVERYTHING in our `medicaid_provider_spending.duckdb` file.

# Setup DuckDB Database
ddb_path = Path("./data/medicaid_provider_spending.duckdb")
# This is a little different.
con = db.connect("md:")
logger.success("Connected to MotherDuck.")

logger.info("Uploading data to MotherDuck.")
con.execute(f"""
create or replace database medicaid_provider_spending
from '{ddb_path}'
;
""")
logger.success("Doesn't it feel good to be done?")

# This takes ~30 minutes because of ADSL and the scale of the data. Importing directly from HuggingFace would have been faster, if it had been possible.

# # 1. Share
#
# - Shares the data with everyone in the organization.
# - That includes me, myself, and I.

con.execute("""
create share if not exists medicaid_provider_spending
from medicaid_provider_spending (
    access organization,
    visibility discoverable,
    update automatic
);
""")
logger.success("Shared medicaid_provider_spending with our organization.")

# # 2. Do Something Else

con.close()
logger.success("Successfully imported data into MotherDuck. Have a nice day!")

# Now, let's alter analysis.py to use our new MotherDuck data.
