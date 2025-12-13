import streamlit as st, math

from streamlit_option_menu import option_menu
from test2 import test2

with st.sidebar:
    selected = option_menu("Main Menu", ["Home", "Settings", "Batasan Normal Suhu"], 
        icons=['house', 'gear', 'checklist'], menu_icon="cast", default_index=1)
    selected

if selected == "Batasan Normal Suhu":
    test2()

st.title("Konversi Suhu")
st.write("Aplikasi konversi suhu sederhana")

# Input nilai suhu
nilai = st.number_input("Masukkan nilai suhu...")

# Pilih satuan derajat asal dan derajat tujuan
dari = st.selectbox("Dari satuan: ", ["Celcius", "Fahrenhait", "Kelvin", "Reamur"])
ke = st.selectbox("Ke satuan: ", ["Celcius", "Fahrenhait", "Kelvin", "Reamur"])

def konversi_suhu(nilai, dari, ke):

    # Konversi ke Celcius
    if dari == "Celcius":
        Celcius = nilai
    elif dari == "Fahrenhait":
        Celcius = (nilai - 32) * 5/9
    elif dari == "Kelvin":
        Celcius = nilai - 273.15
    elif dari == "Reamur":
        Celcius = nilai * 5/4

    # Konversi dari Celcius ke tujuan
    if ke == "Celcius":
        return Celcius
    elif ke == "Fahrenhait":
        return (Celcius * 9/5) + 32
    elif ke == "Kelvin":
        return Celcius + 273.15
    elif ke == "Reamur":
        return Celcius * 4/5
    
# Button konversi suhu
if st.button("Konversi"):
    hasil = konversi_suhu(nilai, dari, ke)
    st.success(f"Maka, hasil konversi dari {dari} ke {ke} adalah {hasil}")