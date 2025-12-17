import streamlit as st, pandas as pd

def info():
    tab1, tab2, tab3 = st.tabs(["Apa Itu Suhu Ruang?", "Apa Itu Suhu Tubuh", " Tabel Batasan Normal Suhu"])
        
    with tab1:
        st.title("Apa Itu Suhu Ruang?")
        st.write("Menurut Organisasi Kesehatan Dunia (WHO), suhu ruang didefinisikan berdasarkan standar kenyamanan dan keamanan kesehatan sebagai berikut: ")
        list1 = ["**Standar Umum:** WHO menetapkan suhu **18°C** sebagai suhu dalam ruangan minimum yang aman bagi orang dewasa sehat dengan pakaian yang sesuai.",
                "**Kelompok Rentan:** Untuk lansia, anak-anak, atau individu dengan kondisi kesehatan tertentu, suhu minimum yang direkomendasikan lebih tinggi, yaitu minimal **20°C**.",
                "**Rentang Kenyamanan:** Dalam konteks hunian dan kesehatan umum, rentang suhu antara **18**°C hingga **24**°C dianggap ideal untuk menjaga kesehatan.",
                "**Konteks Farmasi:** Untuk penyimpanan obat-obatan, WHO mendefinisikan suhu ruangan dalam rentang **+15°C** hingga **25°C**.",]
        for i in list1:
            st.write(f"- {i}")
        st.write("**Catatan Tambahan untuk 2025:**")
        st.write("WHO mnekankan bahwa suhu di atas **24°C** mulai meningkatkan risiko ketidaknyamanan termal, sementara produktivitas pekerja dapat menurun sebesar **2-3%** untuk setiap kenaikan suhu di atas **20°C**.")

    with tab2:
        st.title("Apa Itu Suhu Tubuh?")
        st.write("Organisasi Kesehatan Dunia (WHO) mendefinisikan **suhu tubuh normal** manusia rata-rata berada pada angka **37°C(98,6°F)**. Namun, WHO dan otoritas kesehatan lainnya menekankan bahwa suhu ini bukanlah angka mati, melainkan sebuah rentang yang dipengaruhi oleh berbagai faktor.")
        list2 = ["**Rentang Normal:** Suhu tubuh manusia yang sehat umumnya berkisar antara **36,5°C hingga 37,5°C.**",
                "**Definisi Demam:** Seseorang biasanya dianggap mengalami demam jika suhu tubuhnya mencapai atau melebihi **38°C (100,4°F).**]",
                "**Variasi Harian:** Suhu tubuh tidak statis; biasanya lebih rendah di pagi hari (sekitar pukul 04.00) dan mencapai puncaknya di sore hari (sekitar pukul 16.00–18.00).",]
        for i in list2:
            st.write(f"- {i}")

    with tab3:
        st.title("Tabel Batasan Normal Suhu")
        st.write("Tabel batasan normal suhu.")
        df = pd.DataFrame({
            "Satuan Suhu": ["Celcius", "Fahrenheit", "Kelvin", "Reamur"],
            "Batas Suhu Tubuh": ["36.5 – 37.5", "97.7 – 99.5", "309.65 – 310.65", "29.2 – 30"],
            "Batas Suhu Ruang": ["20 – 25", "68 – 77", "293.15 – 298.15", "16 – 20"]
        })
        df.index = df.index + 1
        st.dataframe(df)
        # st.dataframe(df, hide_index=True) kalo ga mau pake nomor