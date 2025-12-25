import streamlit as st

def person():

    st.markdown("<h1 style='text-align: center;'>🥶 Cek Suhu Tubuh 🥵</h1>", unsafe_allow_html=True)
    
    def konversi_suhu(val, unit):
        if unit == "Celcius": return val
        elif unit == "Fahrenheit": return (val - 32) * 5/9
        elif unit == "Kelvin": return val - 273.15
        elif unit == "Reamur": return val * 5/4

    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("📝 Input Data")
        nilai = st.number_input("Masukkan suhu tubuh:", min_value=0.0, step=0.1)
        satuan = st.selectbox("Pilih satuan suhu:", ["Celcius", "Fahrenheit", "Kelvin", "Reamur"])
        btn_cek = st.button("ANALISIS SEKARANG")

    with col2:
        if btn_cek:
            suhu = konversi_suhu(nilai, satuan)

            st.markdown(f"<h2 style='text-align:center;'>Hasil: {suhu:.2f} °C</h2>", unsafe_allow_html=True)
            
            if 36.5 <= suhu <= 37.5:
                st.success("✅ Kondisi: Normal")
                st.write("Tubuh Anda sehat. Pertahankan gaya hidup seimbang!")
            elif suhu > 37.5:
                st.error("⚠️ Kondisi: DEMAM")
                st.write("Suhu tubuh tinggi. Istirahatlah dan minum banyak cairan.")
            else:
                st.warning("⚠️ Kondisi: HIPOTERMIA")
                st.write("Suhu terlalu rendah. Gunakan pakaian tebal dan segera cari kehangatan.")
        else:
            st.info("Silakan masukkan suhu dan tekan tombol analisis untuk melihat hasil.")