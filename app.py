import streamlit as st

st.title("Débit de pointe – méthode rationnelle")
C = st.slider("Coefficient de ruissellement C", 0.0, 1.0, 0.8)
i = st.number_input("Intensité de pluie (mm/h)", value=50.0)
A = st.number_input("Surface du bassin (ha)", value=2.0)
st.metric("Débit de pointe Q", f"{C * i * A / 360:.3f} m³/s")
