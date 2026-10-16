import streamlit as st

st.title("Débit de pointe – méthode rationnelle")

coefficients = {
    "Toiture": 0.95,
    "Voirie / parking": 0.90,
    "Pavés / dalles": 0.60,
    "Pelouse / espace vert": 0.15,
}

surface = st.selectbox("Type de surface", list(coefficients.keys()))
C = coefficients[surface]
st.write(f"Coefficient de ruissellement retenu : C = {C}")

i = st.number_input("Intensité de pluie (mm/h)", value=50.0)
A = st.number_input("Surface du bassin (ha)", value=2.0)
st.metric("Débit de pointe Q", f"{C * i * A / 360:.3f} m³/s")
