import streamlit as st

def person():
    st.title("Cek Suhu Tubuh")
    st.write("Coba cek kamu demam atau hipotermia:P")

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

        st.write(f"Suhu tubuh kamu: **{suhu:.2f} °C**")

        if 36.5 <= suhu <= 37.5:
            st.success("✅ Suhu tubuh normal")
        elif suhu > 37.5:
            st.warning("⚠️ Suhu tubuh di atas batasan normal. KAMU DEMAM!")
        elif suhu < 36.5:
            st.warning("⚠️ Suhu tubuh di bawah batasan normal. KAMU HIPOTERMIA!")
        else:
            st.warning("⚠️ Suhu tubuh di atas batasan normal. KAMU HIPOTERMIA!")