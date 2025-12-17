import streamlit as st

def room():
    st.title("Rata-rata Suhu Ruangan Harian")
    st.write("Coba cek suhu ruanganmu, kamu lagi di surga😍 atau di neraka🔥:P")
    
    def konversi_suhu(val, unit):
        if unit == "Celcius":
            return val
        elif unit == "Fahrenheit":
            return (val - 32) * 5/9
        elif unit == "Kelvin":
            return val - 273.15
        elif unit == "Reamur":
            return val * 5/4
        
    st.subheader("Input suhu harian")

    satuan = st.selectbox("Satuan Suhu: ", ["Celcius", "Fahrenheit", "Kelvin", "Reamur"])
    
    # Suhu Pagi
    pagi = st.number_input("Suhu Pagi: ")
   
    # Suhu Siang
    siang = st.number_input("Suhu Siang: ")
    
    # Suhu Malam
    malam = st.number_input("Suhu Malam: ")

    if st.button("Cek Rata-rata suhu ruang"):
        suhu_pagi = konversi_suhu(pagi, satuan)
        suhu_siang = konversi_suhu(siang, satuan)
        suhu_malam = konversi_suhu(malam, satuan)

        rata = (suhu_pagi + suhu_siang + suhu_malam) / 3

        st.write(f"Suhu rata-rata kamu: **{rata :.2f} °C**")

        if 20 <= rata <= 25:
            st.success("✅ Suhu ruangan normal")
        elif rata > 25:
            st.warning("⚠️ Suhu ruangan di atas batasan normal. Kamu bisa dehidrasi!")
        elif rata < 20:
            st.warning("⚠️ Suhu tubuh di bawah batasan normal. Kamu bisa hipotermia!")
        else:
            st.warning("⚠️ Suhu tubuh di bawah batasan normal. Kamu bisa hipotermia!")