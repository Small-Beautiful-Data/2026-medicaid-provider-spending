# Medicaid Provider Spending

A featherweight analytics demo!

Uses the Medicaid Provider Spending dataset, releaed by DOGE and HHS on February 13, 2026 for a realistic demo using DuckDB, Ibis, and MotherDuck.

The premise is as commonplace as it is extraordinary. Import a dataset larger thjan available RAM, complete and analysis, and share the data with the team.

Constraints:

- You have no data engineering team.
- You need to have this done, today.

# Agenda

Each of these .py files is intended to be opened as as a Jupytext notebook using Jupyterlab. They will run regardless, but the formatting of the slides may differ if not used in Jupyterlab (dark mode theme). 

- [agenda.py](./agenda.py)
- [import.py](./import.py)
- [analysis.py](./analysis.py)
- [upload.py](./upload.py)
- And then edit [analysis.py](./analysis.py) to run off of MotherDuck.

Due to time constraints (one hour) several parts of this demo were completed in advance.

0. MotherDuck token was generated and stored in a .env file.
1. Data was downloaded from HuggingFace. ~5 minutes
2. Data was uploaded to MotherDuck. ~30 minutes