import streamlit as st

def harian():
    st.set_page_config(
        page_title="Suhu Lingkungan",
        page_icon="🌤️",
        layout="centered"
    )


    st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #74ebd5, #ACB6E5);
    }

    .card {
        padding: 30px;
        border-radius: 20px;
        text-align: center;
        color: white;
        font-size: 22px;
        font-weight: bold;
        margin-top: 30px;
        box-shadow: 0px 10px 25px rgba(0,0,0,0.2);
    }

    .panas {
        background: linear-gradient(135deg, #ff512f, #dd2476);
    }

    .berawan {
        background: linear-gradient(135deg, #2193b0, #6dd5ed);
    }

    .mendung {
        background: linear-gradient(135deg, #757f9a, #d7dde8);
        color: black;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<h1 style='text-align:center;'>🌡️ Suhu Lingkungan</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;'>Menentukan kondisi lingkungan berdasarkan suhu</p>", unsafe_allow_html=True)

    st.divider()


    suhu = st.slider(
        "🌡️ Masukkan suhu lingkungan (°C)",
        min_value=0,
        max_value=45,
        value=27
    )


    if suhu <= 25:
        kondisi = "🌥️ MENDUNG"
        kelas = "mendung"
    elif suhu <= 30:
        kondisi = "☁️ BERAWAN"
        kelas = "berawan"
    else:
        kondisi = "☀️ PANAS"
        kelas = "panas"


    st.markdown(
        f"""
        <div class="card {kelas}">
            <p>Kondisi Lingkungan</p>
            <h2>{kondisi}</h2>
            <p>Suhu: {suhu} °C</p>
        </div>
        """,
        unsafe_allow_html=True
    )


    st.markdown(
        "<p style='text-align:center; font-size:12px; margin-top:20px;'>"
        "Kondisi ditentukan berdasarkan interpretasi suhu, bukan data cuaca resmi."
        "</p>",
        unsafe_allow_html=True
    )
