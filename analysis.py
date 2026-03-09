# # 🪶 Featherweight Analysis
#
# - Our dataset is larger than available RAM, DuckDB churns through it pretty easily.
# - We can analyze our data using regular SQL OR use `Ibis`, a portable dataframe library with more than 20 backends.
#     - The Ibis API exposes a dataframe-like library which is similar to R's `dplyr` syntax.
#     - Ibis uses a backend provider, such as `duckdb` to run the code, translating the instructions into back-end specific SQL.
#     - Porting an analysis from one `Ibis` backend to another is as easy as changing the connection string.
#     - The default output from `Ibis` is pandas, but it can return results as polars dataframes.
#
# ![](./includes/ibis_backends.png)

# +
from pathlib import Path

import altair as alt
import duckdb as db
import ibis
import ibis.expr.datatypes as dt
from dotenv import load_dotenv
from ibis import _
from IPython.display import display, display_html

# We don't need this locally . .
load_dotenv()

alt.theme.enable("dark")
ibis.options.interactive = True
ibis.options.sql.default_limit = 100

# This is how we connected to DuckDB to import the data.
ddb_path = Path("./data/medicaid_provider_spending.duckdb")
ddb_con = db.connect(ddb_path)

# And this is an Ibis connection.
ibis_con = ibis.duckdb.connect("./data/medicaid_provider_spending.duckdb")
ibis_con.list_tables()
# -

# Map mps to our view, vw_medicaid_provider_spending.
# This is similar to how R's dbplyr wors.
mps = ibis_con.table("vw_medicaid_provider_spending").rename("snake_case")
mps

# Use ddb_con to run a SQL query.
# Either way, DuckDB is handling the number crunching.
ddb_con.sql("""
select
     count(*) "Rows"
    ,count(distinct servicing_provider_npi_num) "Distinct Servicing Providers"
    ,count(distinct hcpcs_code) "Distinct HCPCS Codes"
from vw_medicaid_provider_spending
""").df()

# # Analysis - Medicaid Spending By Year
#
# We will complete this analysis using `Ibis`.
#
# The following code chunks will:
#
# - Calculate the total Medicaid spending per year.
# - Show the SQL written by `Ibis` to calculate the total Medicaid spending per year.
# - Chart Medicaid spending per year.
#
# Because services with 12 or fewer rows per month are suppressed, the annual totals shown here are slightly lower than actual.

# Total Medicaid Spending By Year
# This is loosely based on R's dplyr/dbplyr syntax and approach.
mps_by_year = (
    mps
    .group_by(_.claim_from_year)
    .aggregate([
        _.total_claims.sum().name("Total Claims"),
        _.total_paid.sum().round(2).name("Total Paid")
    ])
    .order_by(_.claim_from_year)
    .rename({"Claims From Year":"claim_from_year", })
)
mps_by_year

# The SQL written by Ibis isn't fun to read, but it is SQL.
# Same code as above, but returns the SQL rather than the results.
(
    mps
    .group_by(_.claim_from_year)
    .aggregate([
        _.total_claims.sum().name("Total Claims"),
        _.total_paid.sum().round(2).name("Total Paid")
    ])
    .order_by(_.claim_from_year)
    .rename({"Claims From Year":"claim_from_year", })
    .to_sql()
)

# Chart of total Medicaid Spending By Year
chart_mps = (
    alt.Chart(mps_by_year)
    .mark_line()
    .encode(
        x="Claims From Year",
        y="Total Paid",
        tooltip=["Claims From Year", "Total Paid"],
    )
    .properties(width=600, height=400)
    .interactive()
)
chart_mps

# # Analysis - Medicaid Autism Spending By Year
#
# Looking at a common set of behavioral health services connected to Autism services, we do see a sharp rise in the number of servicing providers and total spent on autism services.

# +
autism_related_services = ["97151", "97152", "97153", "97154", "97155", "97156", "97157", "97158"]

mps_autism_by_year = (
    mps
    .filter(_.hcpcs_code.isin(autism_related_services))
    .group_by(_.claim_from_year)
    .aggregate([
        _.servicing_provider_npi_num.nunique().name("Servicing Providers Providers"),
        _.total_claims.sum().name("Total Claims"),
        _.total_paid.sum().round(2).name("Total Paid")
    ])
    .order_by(_.claim_from_year)
    .rename({"Claims From Year":"claim_from_year", })
)
mps_autism_by_year
# -

# **Important Note:** Minnesota's Early Intensive Developmental and Behavioral Intervention (EIDBI) benefit began
# in 2013. This data does not let us look at service trends from before the fraud allegations.

# Chart of total Medicaid Spending By Year
chart_mps_autism = (
    alt.Chart(mps_autism_by_year)
    .mark_line()
    .encode(
        x="Claims From Year",
        y="Total Paid",
        tooltip=["Claims From Year", "Total Paid"],
    )
    .properties(width=600, height=400)
    .interactive()
)
chart_mps_autism

# # Analysis - Minnesota Medicaid Spending By Year
#
# Just kidding! The Medicaid Provider Spending data does not include a State column so it is not possible to compare Minnesota run this analysis for any individual state. 
#
# The value shown in the Total Paid column is the national total.

ibis_con.disconnect()
ddb_con.close()
