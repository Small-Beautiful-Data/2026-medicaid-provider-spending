# <div style="display: flex; justify-content: flex; align-items: top;">
# <br /><br />
# <div style="flex: 1; text-align: left;">
#     <h2>Did you see this❓</h2>
#     <a href="https://x.com/DOGE_HHS/status/2022370909211021376"><img src="./includes/twitter.png" alt="DOGE@HHS" style="width: 90%;"/></a>
# </div>
# <div style="flex: 1;  justify-content: left;">
#     <h2>Fast Facts:</h2>
#     <ul>
#         <li>Tweeted at 1:02 PM, on Friday the thiteenth (Feb 13, 2026).</li>
#         <li>Published by DOGE on the newly created: <a href="https://opendata.hhs.gov/">opendata.hhs.gov</a></li>
#         <li>Data was taken down less than a week later.</li>
#         <li>Still available on <a href="https://huggingface.co/datasets/HHS-Official/medicaid-provider-spending/viewer">Hugging Face</a> for some reason.</li>
#     </ul>
#     <p>What they said:</p>
#     <blockquote>
#         Today the HHS DOGE team open sourced the largest Medicaid dataset in department history.
#         <br /><br />This dataset contains aggregated, provider-level claims data for specific billing codes over time.
#         <br /><br />For example, using this dataset, it would have been possible to easily detect the large-scale autism diagnosis fraud seen in Minnesota. 
#     </blockquote>
# </div>
# </div>

# <div style="font-size: 1.125rem; display: flex; justify-content: flex; align-items: top;">    
#     <div style="flex: 1;  text-align: left;">
#
# ## A Fowl Challenge
#
# 0. Data larger than available RAM.
# 1. Needs to be shared with stakeholders.
# 2. By When? Today. _Always today._
# 3. No data engineering team.
#         
#     </div>
#     <div style="flex: 1;  text-align: left;">
#         <img src="./includes/share_meme.png" alt="The meme" style="width: 90%; padding: 15px"/></a>
#     </div>
# </div>

# <div style="background-color: #FFFFFF; color:#000000; font-size: 1.125rem; display: flex; justify-content: flex; align-items: center;">    
#     <div style="flex: 1;  text-align: center; ">
#         <img src="./includes/yosemite_sam.svg" alt="Yosemite Sam" style="width: 40%"/></a>
#     </div>
#     <div style="flex: 1;  text-align: left;">
#
# ## Who is this bird-brain?
#
# - Andy Choens
# - Big Yosemite Sam Fan
# - [NYSTEC](https://nystec.com/) Per Diem Consultant
# - [ACPHS](https://www.acphs.edu/) Adjunct: 
#     - Public Health 210 & 211
#     - Public Health 315
# - [Small Beautiful](https://small_beautiful_data.com) Data Owner & Chief Cat Herder
#
#     </div>
# </div>
#
# <div style="background-color: #FFFFFF; color:#000000; display: flex; height: 100px; justify-content: center; align-items: center;">
#     <a href="https://nystec.com/"><img src="./includes/nystec.webp" alt="NYSTEC" style="height: 40px; padding: 30px"/></a>
#     <a href="https://www.acphs.edu/"><img src="./includes/acphs.svg" alt="ACPHS" style="height: 40px; padding: 30px"/></a>
#     <a href="https://small_beautiful_data.com"><img src="./includes/sbd.png" alt="Small Beautiful Data" style="height: 80px; padding: 30px"/></a>
#     <br/>
# </div>
#
# <div style="background-color: #FFFFFF; color:#000000; display: flex; height: 20px; justify-content: center; align-items: center;">
#     <smaller>(SORRY! These logos look better with a light background)</smaler>
# </div>
#
#

# # Introducing Our Goals, Tools, and Data

# </div>
# <div style="font-size: 1.125rem; display: flex; justify-content: space-between;">
#
# <div style="flex: 1; text-align: left;">
#
# ## 🦆  Technical:
#
# 0. Import two datasets from Hugging Face:
#     - Medicaid Provider Spending
#     - HCPCS codes 
# 1. Perform an analysis on the data (Ibis Framework).
# 2. Export data to MotherDuck & share with stakeholders.
# 3. Port our analysis to MotherDuck.
#
# ‼️ Hosting the dashboard is beyond today's scope ‼️
#
# </div>
#
# <div style="flex: 1; text-align: left; ">
#
# ## 🧮  Analytical:
#
# 0. Calculate the total amount spent on Medicaid per year.
# 1. Calculate the number of total number of providers providing Autism-related services per year.
# 2. Calculate the total amount spent per year on Autism services per year.
# 3. Repeat all of the above for the state of Minnesota.
#
# </div>
#
#
# </div>
#
#
#

#
# <div style="background-color: #C0C0C0; display: flex; height: 100px; justify-content: center; align-items: center;">
#    <a href="https://duckdb.org/"><img src="./includes/duckdb_logo.svg" alt="DuckDB Logo" style="height: 75px; padding: 15px"/></a>
#     <a href="https://motherduck.com/"><img src="./includes/motherduck_logo.svg" alt="Mother Duck Logo" style="height: 70px; padding: 15px"/></a>
#     <a href="https://ibis-project.org"><img src="./includes/ibis_logo.svg" alt="Ibis Framework Logo" style="height: 80px; padding: 15px"/></a>
# </div>
#
# <br/>
#
# | Tool           | URL                                           | Fowl Facts                                      |
# | :------------- | :-------------------------------------------- | :---------------------------------------------- |
# | DuckDB         | [duckdb.org](https://duckdb.org/)             | SQLite, for analytics (fast, embedded)          |
# | MotherDuck     | [motherduck.com](https://motherduck.com/)     | Hosted, serverless database (SAAS)              |
# | Ibis Framework | [ibis-project.org](https://ibis-project.org/) | Portable, pythonic dataframe library (our glue) |
#
# <div style="display: flex;  justify-content: center; align-items: center;">
#      <a href="https://huggingface.co"><img src="./includes/huggingface_logo.svg" alt="Hugging Face Logo" style="height: 50px; padding: 45px"/></a>
#      <a href="https://python.org"><img src="./includes/python_logo.png" alt="Python Logo" style="height: 50px; padding: 45px"/></a> 
#      <a href="https://altair-viz.github.io/"><img src="./includes/altair_logo.png" alt="Altair Logo" style="height: 50px; padding: 45px"/></a>
# </div>

# <div style="display: flex; justify-content: space-between;">
# <div style="flex: 1;  justify-content: left; ">
#
# ## Safety Data Sheet
#
# ### Medicaid Provider Spending
#
# - Provides insights into how Medicaid dollars are distributed across providers and procedures nationwide.
# - Medicaid spending data aggregated from outpatient and professional claims with valid HCPCS codes, covering January 2018 through December 2024.
#     - Combinations with fewer than 12 rows suppressed.
#     - Therefore totals will be slightly lower than actual.   
# - Derived from state T-MSIS submissions.
# - 227 Million Rows
# - Distribution Channels:
#     - [OpenData HHS](https://opendata.hhs.gov/) (Currently not accessible)
#     - [Hugging Face - Medicaid Provider Spending](https://huggingface.co/datasets/HHS-Official/medicaid-provider-spending)
# </div>
# <div style="flex: 1;  text-align: right; ">
#     <img src="./includes/sds.png" alt="Safety Data Sheet" style="width: 75%;"/>
# </div>
# </div>
#

# # ⏰ Next Steps:
#
# 0. Install DuckDB & Ibis
# 1. [import.py](./import.py):
#     - Medicaid Provider Spending
#     - HCPCS
#     - Tour of DuckDB CLI and GUI.
# 2. [analysis.py](./analysis.py)
# 3. [upload.py](./upload.py)
# 4. Port analysis to MotherDuck
#
# In the interest of time, some parts of this analysis were completed in advance.
#
# All code is available here: [gitlab.com/small-beautiful-data/demos/2026-medicaid-provider-spending](https://gitlab.com/small-beautiful-data/demos/2026-medicaid-provider-spending)

# # Install DuckDB
#
# ## DuckDB
#
# - Like SQLite, DuckDB is an embedded analytics platform.
# - No database server. Just install the driver for Python, R, DBeaver, etc.
#     - 🪶 Featherweight Analytics!
# - The code below installs the python tooling.
# - As of today, the most recent release is 1.4.4
#
# ```
# uv add duckdb
#
# pip install duckdb
# ```
#
# To learn how to install the CLI app on your platform: [duckdb.org/install/?environment=cli](https://duckdb.org/install/?environment=cli)
#
# ## Ibis Framework
#
# - This would also install DuckDB, if it wasn't already installed.
# - As of today, the most recent release is 12.0.0.
#
# ```
# uv add ibis-framework[duckdb]
#
# pip install ibis-framework[duckdb]
# ```
