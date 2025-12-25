import streamlit as st   

def room():   # PAGE

    st.markdown("""
    <style>
    body {
        background-color: #f0f2f6;
    }

    .title {
        text-align: center;
        font-size: 42px;
        font-weight: bold;
    }

    /* 🔥 PANAS */
    .bg-hot {
        background: linear-gradient(-45deg, #ff0000, #ff7300, #ff0000);
        background-size: 400% 400%;
        animation: fire 5s ease infinite;
    }

    @keyframes fire {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }

    /* ❄️ DINGIN */
    .bg-cold {
        background: linear-gradient(-45deg, #00c6ff, #0072ff, #00c6ff);
        background-size: 400% 400%;
        animation: ice 6s ease infinite;
    }

    @keyframes ice {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }

    /* 😌 NORMAL */
    .bg-normal {
        background: linear-gradient(-45deg, #2ecc71, #a8ff78, #2ecc71);
        background-size: 400% 400%;
        animation: calm 8s ease infinite;
    }

    @keyframes calm {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }
    </style>
    """, unsafe_allow_html=True)

    # HEADER
    st.markdown("<div class='title'>🌡️ Smart Room Temperature System</div>", unsafe_allow_html=True)
    st.caption("Analisis suhu ruangan berdasarkan dampak kesehatan & solusi nyata")

    # FUNCTIOM
    def konversi_suhu(val, unit):
        if unit == "Celcius":
            return val
        elif unit == "Fahrenheit":
            return (val - 32) * 5 / 9
        elif unit == "Kelvin":
            return val - 273.15
        elif unit == "Reamur":
            return val * 5 / 4

    satuan = st.selectbox("🌡️ Pilih Satuan Suhu", ["Celcius", "Fahrenheit", "Kelvin", "Reamur"])

    c1, c2, c3 = st.columns(3)
    with c1:
        pagi = st.number_input("🌅 Suhu Pagi", step=0.1)
    with c2:
        siang = st.number_input("🌞 Suhu Siang", step=0.1)
    with c3:
        malam = st.number_input("🌙 Suhu Malam", step=0.1)

    if st.button("🔍 ANALISIS SUHU RUANGAN", use_container_width=True):

        # VARIABEL
        suhu_pagi = konversi_suhu(pagi, satuan)
        suhu_siang = konversi_suhu(siang, satuan)
        suhu_malam = konversi_suhu(malam, satuan)

        rata = (suhu_pagi + suhu_siang + suhu_malam) / 3

        if rata > 25:
            kondisi = "Panas"
            st.markdown("<script>document.body.className='bg-hot'</script>", unsafe_allow_html=True)
        elif rata < 20:
            kondisi = "Dingin"
            st.markdown("<script>document.body.className='bg-cold'</script>", unsafe_allow_html=True)
        else:
            kondisi = "Normal"
            st.markdown("<script>document.body.className='bg-normal'</script>", unsafe_allow_html=True)

        # HASIL
        st.markdown(f"<h1 style='text-align:center'>{rata:.2f} °C</h1>", unsafe_allow_html=True)

        a, b, c = st.columns(3)
        a.metric("🌅 Pagi", f"{suhu_pagi:.1f} °C")
        b.metric("🌞 Siang", f"{suhu_siang:.1f} °C")
        c.metric("🌙 Malam", f"{suhu_malam:.1f} °C")

        # DAMPAK DAM SOLUSI
        if kondisi == "Panas":
            st.error("🔥 KONDISI PANAS")

            st.markdown("""
            <h3>⚠️ Dampak: Dehidrasi</h3>
            <p>
            Suhu ruangan yang tinggi menyebabkan tubuh mengeluarkan keringat
            secara berlebihan. Hal ini membuat cairan tubuh berkurang lebih cepat,
            sehingga berisiko mengalami <b>dehidrasi</b>.
            </p>
            """, unsafe_allow_html=True)

            dampak_lanjutan = [
                "Lemas dan cepat lelah",
                "Pusing dan sakit kepala",
                "Konsentrasi menurun",
                "Kulit dan mulut terasa kering"
            ]

            solusi = [
                "🥤 Minum air putih setiap 30 menit",
                "❄️ Gunakan kipas atau AC",
                "🪟 Tingkatkan sirkulasi udara",
                "👕 Gunakan pakaian tipis",
                "⏸️ Kurangi aktivitas berat"
            ]

            st.markdown("<h4>🚨 Dampak Lanjutan:</h4>", unsafe_allow_html=True)
            for d in dampak_lanjutan:     
                st.write("-", d)

            st.markdown("<h4>✅ Solusi & Tindakan:</h4>", unsafe_allow_html=True)
            for s in solusi:              
                st.write("-", s)

        elif kondisi == "Dingin":
            st.warning("❄️ KONDISI DINGIN")

            st.markdown("""
            <h3>⚠️ Dampak: Hipotermia</h3>
            <p>
            Suhu ruangan yang terlalu dingin dapat menurunkan suhu tubuh,
            terutama jika terpapar dalam waktu lama.
            </p>
            """, unsafe_allow_html=True)

            dampak_dingin = [
                "Menggigil",
                "Otot terasa kaku",
                "Konsentrasi menurun",
                "Tangan dan kaki terasa dingin"
            ]

            solusi_dingin = [
                "🧥 Gunakan pakaian hangat",
                "🔥 Naikkan suhu ruangan",
                "☕ Konsumsi minuman hangat"
            ]

            for d in dampak_dingin:       
                st.write("-", d)

            for s in solusi_dingin:     
                st.write("-", s)

        else:
            st.success("😌 KONDISI IDEAL")

            dampak_ideal = [
                "Tubuh tetap nyaman",
                "Konsentrasi dan produktivitas meningkat",
                "Risiko gangguan kesehatan rendah"
            ]

            rekomendasi = [
                "Cocok untuk belajar dan bekerja",
                "Efisiensi energi lebih baik"
            ]

            for d in dampak_ideal:        
                st.write("-", d)

            for r in rekomendasi:         
                st.write("-", r)

    st.caption("Smart Room Temperature System • Streamlit")