import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title="SylvaSense",
    page_icon="🌲",
    layout="wide"
)

# TITLE
st.title("🌲 SylvaSense - Forest Monitoring")
st.caption("Forest health and risk monitoring prototype")

# LOAD DATA
file_path = "data/forest_data.csv"

if os.path.exists(file_path):
    df = pd.read_csv(file_path)
else:
    df = pd.DataFrame({
        "area_hectares": [100],
        "canopy_percent": [70]
    })

# FOREST INPUT
st.sidebar.header("🌲 Forest Input")

area = st.sidebar.number_input(
    "Forest Area (hectares)",
    min_value=1.0,
    value=float(df.iloc[0]["area_hectares"])
)

canopy = st.sidebar.slider(
    "Canopy Coverage (%)",
    min_value=0,
    max_value=100,
    value=int(df.iloc[0]["canopy_percent"])
)

# CALCULATIONS
biomass = area * canopy * 2.5
carbon = biomass * 0.47

# FOREST CONDITION
if canopy >= 60:
    condition = "Healthy"
elif canopy >= 30:
    condition = "Moderate"
else:
    condition = "Poor"

# RISK
if canopy >= 60:
    risk = "LOW"
    risk_score = 20
elif canopy >= 30:
    risk = "MEDIUM"
    risk_score = 50
else:
    risk = "HIGH"
    risk_score = 80

# FOREST ANALYSIS
st.header("🌲 Forest Analysis")

st.metric("Canopy Coverage", f"{canopy}%")

if condition == "Healthy":
    st.success("🌿 Predicted Forest Condition: Healthy")
elif condition == "Moderate":
    st.warning("⚠️ Predicted Forest Condition: Moderate")
else:
    st.error("🚨 Predicted Forest Condition: Poor")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("🌿 Canopy Coverage", f"{canopy}%")

with col2:
    st.metric("⚖️ Estimated Biomass", f"{biomass:.2f} t")

with col3:
    st.metric("🌍 Estimated Carbon", f"{carbon:.2f} t")

# RISK ASSESSMENT
st.header("🔵 Forest Risk Assessment")

col4, col5 = st.columns(2)

with col4:
    st.metric("Risk Level", risk)

with col5:
    st.metric("Risk Score", f"{risk_score}/100")

if risk == "LOW":
    st.success("🟢 LOW RISK - Forest condition is currently healthy.")
elif risk == "MEDIUM":
    st.warning("🟡 MEDIUM RISK - Increased monitoring recommended.")
else:
    st.error("🔴 HIGH RISK - Immediate forest inspection recommended.")

# HEALTH OVERVIEW
st.header("📊 Forest Health Overview")

health_data = pd.DataFrame({
    "Indicator": ["Canopy", "Biomass", "Carbon"],
    "Value": [canopy, biomass, carbon]
})

st.bar_chart(health_data.set_index("Indicator"))

# RECOMMENDATIONS
st.header("💡 Recommended Actions")

if risk == "LOW":
    st.success("✅ Continue regular forest monitoring.")
    st.info("🌱 Maintain current forest protection measures.")
elif risk == "MEDIUM":
    st.warning("⚠️ Increase monitoring frequency.")
    st.info("🌱 Consider forest restoration activities.")
else:
    st.error("🚨 Immediate inspection recommended.")
    st.warning("🌱 Prioritize restoration of degraded areas.")

# DATA
st.header("📋 Forest Data")

result = pd.DataFrame({
    "Forest Area (hectares)": [area],
    "Canopy (%)": [canopy],
    "Biomass (tonnes)": [round(biomass, 2)],
    "Carbon (tonnes)": [round(carbon, 2)],
    "Risk": [risk],
    "Condition": [condition]
})

st.dataframe(result, use_container_width=True)

st.divider()
st.caption("SylvaSense Prototype | Forest Monitoring & Environmental Intelligence")