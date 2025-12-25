import streamlit as st, math
# from streamlit_option_menu import option_menu
from info import info
from person import person
from room import room

# with st.sidebar:
#     selected = option_menu("Menu", ["Konversi Suhu", "Batasan Normal Suhu", "Suhu Tubuh", "Suhu Ruang"], 
#         icons=["thermometer",  "table", "person", "building"], menu_icon="cast", default_index=0)
#     selected

st.set_page_config(page_icon="🌡️Konversi Suhu Sederhana", page_title="🌡️Konversi Suhu Sederhana", layout="centered")

st.sidebar.title("🏠Main Menu")
selected = st.sidebar.selectbox("Pilih salah satu menu di bawah ini...", ["🌡️Konversi Suhu", "📝Informasi Terkait Suhu", "🥶Suhu Tubuh🥵", "🏠Suhu Ruang"])

if selected == "🌡️Konversi Suhu":
    st.title("🌡️Konversi Suhu")
    st.write("Aplikasi konversi suhu sederhana.")

    # Input nilai suhu
    nilai = st.number_input("Masukkan nilai suhu...")

    # Pilih satuan derajat asal dan derajat tujuan
    dari = st.selectbox("Dari satuan: ", ["Celcius", "Fahrenhait", "Kelvin", "Reamur"])
    ke = st.selectbox("Ke satuan: ", ["Celcius", "Fahrenhait", "Kelvin", "Reamur"])

    def konversi_suhu(nilai, dari, ke):

        # Konversi ke Celcius
        if dari == "Celcius":
            suhu = nilai
        elif dari == "Fahrenhait":
            suhu = (nilai - 32) * 5/9
        elif dari == "Kelvin":
            suhu = nilai - 273.15
        elif dari == "Reamur":
            suhu = nilai * 5/4

        # Konversi dari Celcius ke tujuan
        if ke == "Celcius":
            return suhu
        elif ke == "Fahrenhait":
            return (suhu * 9/5) + 32
        elif ke == "Kelvin":
            return suhu + 273.15
        elif ke == "Reamur":
            return suhu * 4/5
        
    # Button konversi suhu
    if st.button("Konversi"):
        hasil = konversi_suhu(nilai, dari, ke)
        st.success(f"Maka, hasil konversi dari {dari} ke {ke} adalah {hasil}")

elif selected == "📝Informasi Terkait Suhu":
    info()

elif selected == "🥶Suhu Tubuh🥵":
    person()

elif selected == "🏠Suhu Ruang":
    room()

