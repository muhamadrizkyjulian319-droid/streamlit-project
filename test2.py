import streamlit as st, pandas as pd

def test2():
    st.title("Batasan Normal Suhu")
    df = pd.DataFrame({
        "Satuan Suhu": ["Celcius", "Fahrenheit", "Kelvin", "Reamur"],
        "Batas Ruang": ["20–25", "68–77", "293.15–298.15", "16–20"],
        "Batas Tubuh": ["36.5–37.5", "97.7–99.5", "309.65–310.65", "29.2–30"]
    })
    st.dataframe(df)