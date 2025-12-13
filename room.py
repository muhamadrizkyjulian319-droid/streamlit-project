import streamlit as st

def room():
    st.title("Cek Suhu Ruang")
    st.write("Coba cek suhu ruanganmu, kamu lagi di surga atau di neraka:P")

    nilai = st.number_input("Masukkan suhu tubuh: ")
    satuan = st.selectbox("Pilih satuan suhu: ", ["Celcius", "Fahrenheit", "Kelvin", "Reamur"])

    # Konversi ke Celcius
    def konversi_suhu(val, unit):
        if unit == "Celcius":
            return val
        elif unit == "Fahrenheit":
            return (val - 32) * 5/9
        elif unit == "Kelvin":
            return val - 273.15
        elif unit == "Reamur":
            return val * 5/4

    if st.button("Cek Suhu Tubuh"):
        suhu = konversi_suhu(nilai, satuan)

        if 20 <= suhu <= 25:
            st.success("✅ Suhu ruangan normal")
        elif suhu > 25:
            st.warning("⚠️ Suhu ruangan di atas batasan normal. Kamu bisa dehidrasi!")
        elif suhu < 20:
            st.warning("⚠️ Suhu tubuh di bawah batasan normal. Kamu bisa hipotermia!")
        else:
            st.warning("⚠️ Suhu tubuh di bawah batasan normal. Kamu bisa hipotermia!")