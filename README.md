
# Solar Challenge Week 0

## Project Overview
This repository contains EDA and Streamlit dashboard for solar farm analysis across Benin, Sierra Leone, and Togo.

## Folder Structure
- `notebooks/` : EDA notebooks for each country and cross-country comparison
- `app/`       : Streamlit dashboard skeleton
- `data/`      : Cleaned datasets (ignored in Git)

## How to Run
1. Create and activate a virtual environment:


## Setup Instructions
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt

---

### 2. **requirements.txt**
Create a file `requirements.txt` that includes all libraries used so far:

```text
pandas
numpy
matplotlib
seaborn
scipy
streamlit
solar-challenge-week0/
│
├── data/
│   ├── raw/
│   │   └── sierraleone-bumbuna.csv
│   └── clean/
│       └── sierraleone-bumbuna-clean.csv
│
├── notebooks/
│   └── sierraleone_analysis.ipynb
│
├── app/
│   └── dashboard.py     ← (will come later in dashboard branch)
│
├── README.md
├── requirements.txt
└── .gitignore
