import streamlit as st, pandas as pd

def table():
    st.title("Batasan Normal Suhu")
    st.write("Tabel batasan normal suhu.")
    df = pd.DataFrame({
        "Satuan Suhu": ["Celcius", "Fahrenheit", "Kelvin", "Reamur"],
        "Batas Suhu Tubuh": ["36.5 – 37.5", "97.7 – 99.5", "309.65 – 310.65", "29.2 – 30"],
        "Batas Suhu Ruang": ["20 – 25", "68 – 77", "293.15 – 298.15", "16 – 20"]
    })
    df.index = df.index + 1
    st.dataframe(df)
    # st.dataframe(df, hide_index=True) kalo mau ga pake nomor