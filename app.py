import streamlit as st
import yt_dlp
import os

# Sayfa Ayarları
st.set_page_config(page_title="ShrTube | Modern İndirici", page_icon="⚡", layout="centered")

# CSS ve Stil Motoru (Siber Yazı Tipi ve Logo)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@800&display=swap');
    .stApp { background-color: #000000; color: #ffffff; }
    
    /* LOGO VE BAŞLIK */
    .logo-container { text-align: center; margin-bottom: 10px; }
    .brand-name { 
        font-family: 'Orbitron', sans-serif; 
        font-size: 60px; 
        background: linear-gradient(90deg, #00f2fe, #a259ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0px;
    }
    
    /* KAYAR LED */
    .led-container {
        width: 100%; background-color: #0a0a0f; border-top: 2px solid #8a2be2; 
        border-bottom: 2px solid #00f2fe; padding: 10px 0; overflow: hidden; margin: 20px 0;
    }
    .led-text {
        white-space: nowrap; animation: kayar 12s linear infinite; font-weight: 800;
        font-size: 14px; letter-spacing: 2px; color: #00f2fe;
    }
    @keyframes kayar { 0% { transform: translateX(100%); } 100% { transform: translateX(-100%); } }
    
    .stTextInput>div>div>input { background: #12121c !important; border: 1px solid #333; color: white !important; border-radius: 8px; }
    .stButton>button { width: 100%; border-radius: 8px; font-weight: bold; padding: 12px; transition: 0.3s; }
</style>
""", unsafe_allow_html=True)

# LOGO VE BAŞLIK
st.markdown("""
<div class='logo-container'>
    <svg width="80" height="80" viewBox="0 0 100 100">
        <defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#00f2fe"/><stop offset="100%" stop-color="#8a2be2"/></linearGradient></defs>
        <path d="M50 5 L95 25 L95 75 L50 95 L5 75 L5 25 Z" fill="none" stroke="url(#g)" stroke-width="6"/>
        <path d="M30 40 L70 40 L50 70 Z" fill="url(#g)"/>
    </svg>
    <div class='brand-name'>SHRTUBE</div>
</div>
""", unsafe_allow_html=True)

# LED ŞERİT
st.markdown("""
<div class='led-container'>
    <div class='led-text'>⚡ YÜKSEK HIZLI SHORTS İNDİRME AKTİF • MP4 & MP3 MODU • SİBER TASARIM ⚡</div>
</div>
""", unsafe_allow_html=True)

url = st.text_input("Shorts Linkini Buraya Yapıştır:", placeholder="https://youtube.com/shorts/...")

col1, col2 = st.columns(2)

def indir(video_url, mod):
    if not video_url:
        st.error("Link girmedin kanka!")
        return
    with st.spinner("İşleniyor..."):
        try:
            ydl_opts = {
                'quiet': True, 'no_warnings': True, 'nocheckcertificate': True,
                'format': 'best' if mod == "mp4" else 'bestaudio/best',
                'outtmpl': 'download.%(ext)s',
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(video_url, download=True)
                dosya = f"download.{info.get('ext')}"
                with open(dosya, "rb") as f:
                    st.download_button(
                        label=f"💾 {'MP4 Video İndir' if mod=='mp4' else 'MP3 Ses İndir'}",
                        data=f, file_name=f"{info.get('title')}.{mod}",
                        mime="video/mp4" if mod == "mp4" else "audio/mpeg"
                    )
            if os.path.exists(dosya): os.remove(dosya)
        except Exception as e:
            st.error(f"Hata: {e}")

with col1:
    if st.button("🎥 MP4 Video İndir"): indir(url, "mp4")
with col2:
    if st.button("🎵 MP3 Ses İndir"): indir(url, "mp3")