import streamlit as st
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

st.title("🌳 SylvaSense")
st.markdown("### AI-Powered Forest Monitoring & Carbon Intelligence")
st.caption("🌍 Analyze forest canopy, estimate biomass, measure carbon, and assess forest risk.")
# Load dataset
data = pd.read_csv("data/forest_data.csv")

# Train AI model
X = data[["canopy_percent"]]
y = pd.cut(data["canopy_percent"], bins=[-1, 30, 60, 100], labels=["Poor", "Moderate", "Healthy"])
model = DecisionTreeClassifier()
model.fit(X, y)

# User input
canopy = st.slider(
    "Select Forest Canopy Coverage (%)",
    0, 100, 70
)

# Prediction
prediction = model.predict([[canopy]])[0]

st.write("### 🌲 Forest Analysis")

st.metric("Canopy Coverage", f"{canopy}%")
st.success(f"Predicted Forest Condition: {prediction}")

# Simple biomass and carbon estimation
area = 120
biomass = area * canopy * 2.5 / 100
carbon = biomass * 0.47

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("🌳 Canopy Coverage", f"{canopy}%")

with col2:
    st.metric("🌿 Estimated Biomass", f"{biomass:.2f} t")

with col3:
    st.metric("🌍 Estimated Carbon", f"{carbon:.2f} t")
st.subheader("🌍 Forest Risk Assessment")
st.subheader("📊 Forest Health Overview")

chart_data = pd.DataFrame({
    "Metric": ["Canopy Coverage", "Biomass", "Carbon"],
    "Value": [canopy, biomass, carbon]
})

st.bar_chart(chart_data.set_index("Metric"))
if canopy < 30:
    st.error("🔴 HIGH RISK — Immediate forest protection required.")
elif canopy < 60:
    st.warning("🟡 MODERATE RISK — Increase monitoring and protect vegetation.")
else:
    st.success("🟢 LOW RISK — Forest condition is currently healthy.")
if canopy < 30:
    st.warning("⚠️ Low canopy coverage detected!")
else:
    st.info("✅ Forest canopy condition looks healthy.")
if canopy < 30:
    st.error("🚨 Recommended Action: Reforestation and immediate forest protection.")
elif canopy < 60:
    st.warning("⚠️ Recommended Action: Increase monitoring and protect existing vegetation.")
else:
    st.success("✅ Recommended Action: Continue regular forest monitoring.")