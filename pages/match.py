import streamlit as st
import pandas as pd
from api.sentiment_gpt import ask_gpt
from algorithms.moviesPredictor import predict

predictor = predict()

# --- Page Config ---
st.set_page_config(
    page_title="MovieMatch — Find Your Match",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- Header ---
st.title("🎯 Movie Selection")
st.caption("Select 3 movies you love and let our AI find your next favorites")

st.divider()

import os

# --- Load Movies ---
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
csv_path = os.path.join(base_dir, 'assets', 'files', 'moviesdos.csv')
with open(csv_path, 'r', encoding='utf-8') as file:
    movies = file.readlines()
movies = [movie.strip() for movie in movies]

# --- Movie Selection ---
st.subheader("📽️ Choose Your 3 Favorites")
st.write("Search and pick exactly 3 movies from 4,800+ titles")
st.write("")

selected_movies = st.multiselect(
    label="Search movies",
    options=movies,
    default=movies[:3],
    max_selections=3,
)

# --- Show Selected Movies as Cards ---
if selected_movies:
    st.write("")
    cols = st.columns(len(selected_movies))
    for i, movie in enumerate(selected_movies):
        with cols[i]:
            with st.container(border=True):
                st.caption(f"PICK #{i+1}")
                st.write(f"**{movie}**")

st.write("")

# --- Get Recommendations ---
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    get_recs = st.button("🔮 Get Recommendations", use_container_width=True)

if get_recs:
    if len(selected_movies) < 3:
        st.error("❌ Please select exactly 3 movies before getting recommendations.")
    else:
        with st.spinner("🧠 Analyzing similarity across genres, cast, directors, and keywords..."):
            recommendations = predictor.moviePreds(selected_movies)

        st.divider()
        st.subheader("✨ Your Recommendations")
        st.write("")

        rank_labels = ["🥇 Top Pick", "🥈 Runner Up", "🎯 Great Match", "💎 Hidden Gem"]
        rec_cols = st.columns(len(recommendations))

        for i, rec in enumerate(recommendations):
            with rec_cols[i]:
                with st.container(border=True):
                    st.caption(rank_labels[i] if i < len(rank_labels) else f"Match #{i+1}")
                    st.write(f"**{rec}**")

        st.balloons()
        st.success(f"🎉 Found {len(recommendations)} movies you'll love!")

# --- Sentiment Analysis Section ---
st.divider()

st.subheader("💬 Share Your Thoughts")
st.write("Tell us how you feel about the recommendations — our AI will analyze your sentiment in real time.")
st.write("")

prompt = st.text_area(
    "Your feedback",
    placeholder="e.g., I loved the recommendations! The movies match my taste perfectly...",
    height=120,
)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    submit_sentiment = st.button("🤖 Analyze My Sentiment", use_container_width=True)

if submit_sentiment:
    if not prompt or prompt.strip() == "":
        st.warning("⚠️ Please type your feedback first!")
    else:
        with st.spinner("🤖 Gemini is analyzing your sentiment..."):
            response = ask_gpt(prompt)

        st.divider()
        st.subheader("🧠 Sentiment Analysis Result")
        st.info(response)

# --- Footer ---
st.divider()
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.page_link("pages/report a bug.py", label="🐞 Report a Bug")
