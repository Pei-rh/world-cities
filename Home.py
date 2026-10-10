import streamlit as st

st.set_page_config(
    page_title="World Cities App",
    page_icon="🌍",
    layout="centered",
)

# Custom styling
st.markdown("""
    <style>
        .main-title {
            text-align: center;
            color: #1f77b4;
            margin-bottom: 20px;
        }
        .welcome-text {
            text-align: center;
            font-size: 18px;
            color: #555;
            margin-bottom: 30px;
        }
    </style>
    """, unsafe_allow_html=True)

# Display title and welcome message
st.markdown("<h1 class='main-title'>🌍 World Cities Explorer</h1>", unsafe_allow_html=True)
st.markdown("<p class='welcome-text'>Welcome to the World Cities App! Explore cities from around the globe and discover fascinating information.</p>", unsafe_allow_html=True)

# Display some intro content
st.write("""
This multipage application helps you explore and learn about cities worldwide. 
Navigate to the different sections using the sidebar to get started.
""")

# Button to navigate to app.py
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    if st.button("🚀 Go to App", key="go_to_app", use_container_width=True):
        st.switch_page("pages/app.py")

# Display additional information
st.divider()
st.subheader("✨ Features")
st.write("""
- 📍 Browse cities by region
- 🏙️ View detailed city information
- 🗺️ Interactive maps and data visualizations
- 💾 Save your favorite cities
""")
