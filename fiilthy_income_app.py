import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import requests
import time
import random
from datetime import datetime, timedelta

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="FiiLTHY Income Dashboard",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- STYLE ---
st.markdown("""
    <style>
    .main {
        background-color: #05060a;
        color: #ffffff;
    }
    .stButton>button {
        background-color: #ff005f;
        color: white;
        border-radius: 10px;
        border: none;
        font-weight: bold;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #cc004c;
        box-shadow: 0px 0px 15px #ff005f;
    }
    .stSidebar {
        background-color: #0d1117;
    }
    h1, h2, h3 {
        color: #ff005f;
        text-shadow: 2px 2px 10px rgba(255, 0, 95, 0.3);
    }
    .metric-card {
        background-color: #161b22;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #30363d;
        text-align: center;
    }
    .status-badge {
        padding: 5px 10px;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: bold;
    }
    .status-live { background-color: #238636; color: white; }
    .status-pending { background-color: #d29922; color: white; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR / CONFIG ---
with st.sidebar:
    st.image("https://avatars.githubusercontent.com/u/274173531?s=200&v=4", width=100)
    st.title("FiiLTHY.ai")
    st.markdown("---")
    backend_url = st.text_input("Vercel Backend URL", value="https://fiilthy-api.vercel.app")
    st.markdown("---")
    st.info("System Status: 🚀 ONLINE")
    st.sidebar.markdown("© 2026 FiiLTHY.ai Factory")

# --- MOCK DATA GENERATORS ---
def get_mock_opportunities():
    niches = ["AI Writing Tools", "Sustainable Fashion", "Home Workout Gear", "Digital Planners", "TikTok Ads Masterclass"]
    return [
        {
            "id": f"opp-{i}",
            "title": niches[i % len(niches)],
            "commission": f"{random.randint(15, 45)}%",
            "viral_score": random.randint(75, 99),
            "potential": f"${random.randint(500, 5000)}/mo",
            "competition": random.choice(["Low", "Medium", "High"])
        } for i in range(5)
    ]

# --- APP LAYOUT ---
st.title("🚀 FiiLTHY INCOME DASHBOARD")
st.markdown("Transforming AI Factory output into raw profit. 💸")

tab1, tab2, tab3, tab4 = st.tabs(["🎯 Opportunity Hunter", "🎬 Video Lab", "📉 Profit Tracking", "⚙️ System Blast"])

# --- TAB 1: OPPORTUNITY HUNTER ---
with tab1:
    st.header("🎯 Target Acquired")
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("Scan Parameters")
        st.selectbox("Category", ["Affiliate Marketing", "Digital Products", "SaaS Tools"])
        st.slider("Min Viral Score", 0, 100, 80)
        if st.button("SCAN FOR PROFITS 🔍"):
            with st.spinner("Analyzing market trends..."):
                time.sleep(2)
                st.session_state.opps = get_mock_opportunities()
                st.success("Targeting profitable niches!")

    with col2:
        if "opps" in st.session_state:
            for opp in st.session_state.opps:
                with st.expander(f"{opp['title']} (Viral Score: {opp['viral_score']})"):
                    c1, c2, c3 = st.columns(3)
                    c1.metric("Commission", opp['commission'])
                    c2.metric("Potential", opp['potential'])
                    c3.metric("Competition", opp['competition'])
                    if st.button(f"Generate Content for {opp['id']}", key=opp['id']):
                        st.session_state.active_target = opp
                        st.toast(f"Locked on: {opp['title']}")

# --- TAB 2: VIDEO LAB ---
with tab2:
    st.header("🎬 AI Content Factory")
    if "active_target" in st.session_state:
        target = st.session_state.active_target
        st.info(f"Generating viral content for: **{target['title']}**")
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.subheader("Production Settings")
            st.selectbox("Style", ["High-Energy Review", "Educational/How-To", "Problem/Solution Aesthetic"])
            st.selectbox("Voice", ["Professional Male", "Enthusiastic Female", "Deep Cinematic"])
            
            if st.button("BUILD VIDEO NOW 🛠️"):
                progress_bar = st.progress(0)
                status_text = st.empty()
                for percent_complete in range(100):
                    time.sleep(0.05)
                    progress_bar.progress(percent_complete + 1)
                    if percent_complete < 30: status_text.text("🤖 Generating AI Script...")
                    elif percent_complete < 60: status_text.text("🎞️ Fetching Pexels Assets...")
                    elif percent_complete < 90: status_text.text("🎙️ Generating ElevenLabs Voiceover...")
                    else: status_text.text("✅ Rendering Final MP4...")
                st.session_state.video_ready = True
                st.success("Video Rendered Successfully!")

        with col2:
            st.subheader("Quality Control Preview")
            if "video_ready" in st.session_state:
                st.video("https://www.w3schools.com/html/mov_bbb.mp4") # Placeholder
                st.markdown("### QC Score: **94/100** ⚡")
                st.markdown("- ✅ Hook is under 2 seconds\n- ✅ High contrast visuals\n- ✅ Subtitles synchronized\n- ⚠️ Add trending sound for +5% boost")
            else:
                st.warning("No video rendered yet. Hit 'BUILD VIDEO' to start.")
    else:
        st.warning("Please select a target in the Opportunity Hunter tab first.")

# --- TAB 3: PROFIT TRACKING ---
with tab3:
    st.header("📉 Revenue attribution")
    
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Total Profit", "$1,240.50", "+12%")
    m2.metric("Active Campaigns", "4", "+1")
    m3.metric("Total Views", "85.2K", "+45%")
    m4.metric("Conversion Rate", "2.4%", "+0.5%")
    
    # Chart
    df = pd.DataFrame({
        'Date': pd.date_range(start='2026-04-01', periods=14),
        'Revenue': [100, 150, 80, 200, 300, 250, 400, 380, 500, 600, 550, 700, 850, 1100]
    })
    fig = px.line(df, x='Date', y='Revenue', title='Revenue Growth (14 Days)', template='plotly_dark')
    fig.update_traces(line_color='#ff005f', line_width=4)
    st.plotly_chart(fig, use_container_view_width=True)

# --- TAB 4: SYSTEM BLAST ---
with tab4:
    st.header("⚙️ Platform Blast Center")
    st.markdown("Schedule and deploy content across the grid.")
    
    platforms = [
        {"name": "TikTok", "status": "LIVE", "handle": "@fiilthy_hustle"},
        {"name": "Instagram", "status": "LIVE", "handle": "@fiilthy_results"},
        {"name": "YouTube Shorts", "status": "PENDING", "handle": "FiiLTHY AI"},
    ]
    
    for p in platforms:
        with st.container():
            col1, col2, col3 = st.columns([1, 1, 1])
            col1.write(f"**{p['name']}**")
            col2.write(f"Account: `{p['handle']}`")
            status_class = "status-live" if p['status'] == "LIVE" else "status-pending"
            col3.markdown(f'<span class="status-badge {status_class}">{p["status"]}</span>', unsafe_allow_html=True)
            st.markdown("---")
            
    if st.button("BLAST ALL CHANNELS 🚀"):
        st.balloons()
        st.success("Deployment sequence initiated across all platforms!")