# Solar Challenge Week 0 - Setup Task

This project analyzes solar radiation data for multiple countries.

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
