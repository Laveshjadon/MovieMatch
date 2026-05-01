import streamlit as st

# --- Page Config ---
st.set_page_config(
    page_title="MovieMatch — Smart Recommendations",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- Hero Section ---
st.title("🎬 MovieMatch")
st.caption("Select 3 movies you love → Get intelligent recommendations powered by AI")

st.divider()

# --- Stats ---
col1, col2, col3, col4 = st.columns(4)
col1.metric("🎥 Movies", "4,800+")
col2.metric("📐 Features", "4 Dimensions")
col3.metric("🤖 AI Engine", "Gemini")
col4.metric("⚡ Speed", "< 5 sec")

st.divider()

# --- Feature Cards ---
st.subheader("What Makes MovieMatch Special")
st.write("")

col1, col2, col3 = st.columns(3)

with col1:
    with st.container(border=True):
        st.subheader("🧠 Smart Similarity")
        st.write("Analyzes genres, cast, directors, and plot keywords simultaneously using cosine distance for deep content matching.")

with col2:
    with st.container(border=True):
        st.subheader("🎯 Pair Detection")
        st.write("Identifies the strongest taste signal from your 3 picks and generates recommendations aligned with your preferences.")

with col3:
    with st.container(border=True):
        st.subheader("💬 Sentiment Analysis")
        st.write("Share your thoughts on recommendations and receive real-time AI-powered emotional tone analysis via Google Gemini.")

st.divider()

# --- How It Works ---
st.subheader("How It Works")
st.write("")

col1, col2, col3, col4 = st.columns(4)

with col1:
    with st.container(border=True):
        st.write("**Step 1️⃣**")
        st.write("Select 3 movies from our database of 4,800+ titles")

with col2:
    with st.container(border=True):
        st.write("**Step 2️⃣**")
        st.write("Engine computes multi-feature cosine similarity across all pairs")

with col3:
    with st.container(border=True):
        st.write("**Step 3️⃣**")
        st.write("Strongest pair is identified and 4 recommendations are generated")

with col4:
    with st.container(border=True):
        st.write("**Step 4️⃣**")
        st.write("Share feedback and get AI sentiment analysis")

st.divider()

# --- CTA ---
st.subheader("🚀 Ready to find your next favorite movie?")
st.write("Click below to start the matching process")
st.write("")

st.page_link("pages/match.py", label="🚀 Start Matching", icon="🎬")