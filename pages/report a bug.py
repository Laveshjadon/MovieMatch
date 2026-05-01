import streamlit as st

# --- Page Config ---
st.set_page_config(
    page_title="MovieMatch — Report a Bug",
    page_icon="🐞",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- Header ---
st.title("🐞 Bug Report")
st.caption("Found something broken? Help us improve MovieMatch by reporting the issue below.")

st.divider()

# --- Bug Report Form ---
with st.container(border=True):
    bug_type = st.selectbox(
        "What type of issue did you encounter?",
        ["Recommendation Quality", "App Crash / Error", "UI / Display Issue", "Sentiment Analysis Issue", "Other"]
    )

    bug_description = st.text_area(
        "Describe the bug in detail",
        placeholder="Tell us what happened, what you expected, and steps to reproduce the issue...",
        height=150
    )

    user_email = st.text_input(
        "Your email (optional)",
        placeholder="your@email.com"
    )

    attachment = st.file_uploader(
        "Attach screenshots or files (optional)",
        type=["png", "jpg", "jpeg", "pdf", "txt"]
    )

    st.write("")

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("📨 Submit Bug Report", use_container_width=True):
            if not bug_description or bug_description.strip() == "":
                st.warning("⚠️ Please describe the bug before submitting.")
            else:
                st.success("✅ Bug report submitted successfully! Thank you for helping us improve MovieMatch.")
                st.balloons()

# --- Footer ---
st.divider()
st.caption("Thank you for choosing MovieMatch 🎬")
