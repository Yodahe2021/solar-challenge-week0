import streamlit as st

st.title("🎈 My new app")
st.title("🎈 My new Streamlit app")

import pandas as pd

@st.cache_data
def load_data(country):
    return pd.read_csv(f"data/clean/{country}-clean.csv")

country = st.selectbox("Select Country", ["benin-malanville-clean", "sierra_leone-malanville-clean", "togo-dapaong_qc-clean"])
df = load_data(country)
st.write(df.head())
import matplotlib.pyplot as plt
import seaborn as sns

variable = st.selectbox("Select variable to visualize", ["GHI", "DNI", "DHI", "Tamb"])

fig, ax = plt.subplots()
sns.lineplot(data=df, x="Timestamp", y=variable, ax=ax)
st.pyplot(fig)
st.subheader("Summary Statistics")
st.write(df.describe())
