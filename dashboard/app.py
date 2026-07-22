import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Forecasting Financial Inclusion in Ethiopia",
    layout="wide"
)

st.title("Forecasting Financial Inclusion in Ethiopia")

st.write(
    "Interactive dashboard for exploring Ethiopia's financial inclusion dataset and forecasting results."
)

# Load dataset
data = pd.read_excel("data/raw/ethiopia_fi_unified_data.xlsx")

# Show dataset
st.header("Dataset Preview")
st.dataframe(data.head())

# Basic metrics
st.header("Dataset Summary")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Records", len(data))

with col2:
    st.metric("Indicators", data["indicator_code"].nunique())

with col3:
    st.metric("Source Types", data["source_type"].nunique())

# Visualizations
st.header("Exploratory Data Analysis")

st.image("reports/figures/record_type_distribution.png")

st.image("reports/figures/pillar_distribution.png")

st.image("reports/figures/confidence_distribution.png")

st.image("reports/figures/source_type_distribution.png")

st.image("reports/figures/temporal_coverage.png")

st.image("reports/figures/account_ownership.png")

st.image("reports/figures/mobile_money_account.png")

# Forecasts
st.header("Forecast Results")

st.image("reports/forecast_access.png")

st.image("reports/forecast_mobile_money.png")

# Insights
st.header("Key Findings")

st.markdown("""
- Access indicators dominate the dataset.
- Usage indicators continue growing.
- Telebirr significantly accelerated mobile money adoption.
- Most observations are high confidence.
- Historical observations remain limited, increasing forecast uncertainty.
""")

# Download
st.header("Download Dataset")

csv = data.to_csv(index=False)

st.download_button(
    label="Download Dataset",
    data=csv,
    file_name="ethiopia_financial_inclusion.csv",
    mime="text/csv"
)