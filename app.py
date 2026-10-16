import streamlit as st
import pandas as pd

st.set_page_config(page_title="Débit de pointe", page_icon="💧")

st.title("Débit de pointe – méthode rationnelle")
st.caption("Estimation du débit de pointe ruisselé sur un petit bassin versant urbain.")

coefficients = {
    "Toiture": 0.95,
    "Toiture végétalisée": 0.40,
    "Voirie / parking": 0.90,
    "Pavés / dalles": 0.60,
    "Pelouse / espace vert": 0.15,
}

st.sidebar.header("Paramètres")
surface = st.sidebar.selectbox("Type de surface", list(coefficients.keys()))
C = coefficients[surface]
i = st.sidebar.number_input("Intensité de pluie (mm/h)", min_value=0.0, value=50.0)
A = st.sidebar.number_input("Surface du bassin (ha)", min_value=0.0, value=2.0)

Q = C * i * A / 360

col1, col2, col3 = st.columns(3)
col1.metric("Coefficient C", C)
col2.metric("Surface", f"{A} ha")
col3.metric("Débit de pointe Q", f"{Q:.3f} m³/s")

with st.expander("Comment est calculé le débit ?"):
    st.latex(r"Q = \frac{C \times i \times A}{360}")
    st.markdown(
        """
- **Q** : débit de pointe (m³/s)
- **C** : coefficient de ruissellement (sans unité)
- **i** : intensité de pluie (mm/h), pour une durée égale au temps de concentration
- **A** : surface du bassin versant (ha)

Le facteur 360 sert à convertir les unités (mm/h × ha → m³/s).
La méthode rationnelle ne s'applique qu'aux petits bassins versants.
"""
    )

st.subheader("Débit selon l'intensité de pluie")

intensites = []
debits = []
for intensite in range(10, 151, 10):
    intensites.append(intensite)
    debits.append(C * intensite * A / 360)

tableau = pd.DataFrame({"Intensité (mm/h)": intensites, "Débit Q (m³/s)": debits})
st.line_chart(tableau.set_index("Intensité (mm/h)"))
