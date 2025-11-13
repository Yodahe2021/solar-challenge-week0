import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set the app title
st.title("🎈 My new Streamlit app")

# Cache data loading for performance
@st.cache_data
def load_data(country):
    return pd.read_csv(f"data/clean/{country}-clean.csv")

# Dropdown to select a country
country = st.selectbox(
    "Select Country",
    ["benin-malanville", "sierra_leone-malanville", "togo-dapaong_qc"]
)

# Load the selected data
df = load_data(country)

# Show a sample of the data
st.write(df.head())

# Select a variable to visualize
variable = st.selectbox(
    "Select variable to visualize",
    ["GHI", "DNI", "DHI", "Tamb"]
)

# Plot the selected variable
fig, ax = plt.subplots()
sns.lineplot(data=df, x="Timestamp", y=variable, ax=ax)
ax.set_title(f"{variable} over time in {country}")
st.pyplot(fig)

# Display summary statistics
st.subheader("Summary Statistics")
st.write(df.describe())
