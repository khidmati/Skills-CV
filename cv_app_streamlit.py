import streamlit as st
import json

# Load custom font and add rounded, bright styling
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');
    
    .reportview-container {
        font-family: 'Poppins', sans-serif;
        background-color: #f0f4f8;
    }
    .main {
        color: #1a1a1a;
    }
    .headline {
        font-size: 40px;
        color: #007acc;
        font-weight: 600;
        text-align: center;
        padding-top: 10px;
        padding-bottom: 20px;
    }
    .title {
        font-size: 26px;
        color: #555;
        font-weight: 500;
        text-align: center;
    }
    .body-text {
        font-size: 22px;
        color: #333;
        font-weight: 400;
        text-align: center;
        margin-bottom: 10px;
    }
    .stTextInput > div > input {
        font-size: 20px !important;
        color: #333;
        padding: 15px !important;
        background-color: #ffffff;
        border-radius: 10px;
        border: 1px solid #ccc;
    }
    .stTextInput > div > input::placeholder {
        color: #888;
    }
    .stButton > button {
        font-size: 18px;
        padding: 10px 20px;
        border-radius: 20px;
        background-color: #007acc;
        color: #fff;
        border: none;
        transition: background-color 0.3s;
    }
    .stButton > button:hover {
        background-color: #005f9e;
    }
    .progress {
        width: 100%;
        background-color: #e0e0e0;
        border-radius: 20px;
        margin-top: 20px;
        margin-bottom: 20px;
    }
    .progress-bar {
        width: {progress}%;
        height: 24px;
        background-color: #4caf50;
        border-radius: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Define mode and questions
mode = st.sidebar.radio("Select Mode", ["Day Mode", "Night Mode"])
questions = {
    "Personal Information": [
        "What is your full name?",
        "What is your primary contact information (phone number and email address)?",
        "What is your current location (City, Postcode)?",
        "Do you have any online professional profiles (LinkedIn, website, portfolio link)?"
    ],
    # Additional sections here
}

# Set session state for responses and progress
if "responses" not in st.session_state:
    st.session_state.responses = {}
if "progress" not in st.session_state:
    st.session_state.progress = 0

# Display headline
st.markdown("<div class='headline'>Student CV Generator</div>", unsafe_allow_html=True)
st.markdown(f"<div class='title'>Progress: {st.session_state.progress}%</div>", unsafe_allow_html=True)

# Display progress bar
st.markdown(
    f"<div class='progress'><div class='progress-bar' style='width: {st.session_state.progress}%'></div></div>",
    unsafe_allow_html=True
)

# Display current section and question
for section, qs in questions.items():
    st.markdown(f"<div class='title'>{section}</div>", unsafe_allow_html=True)
    for q in qs:
        st.markdown(f"<div class='body-text'>{q}</div>", unsafe_allow_html=True)
        st.text_input("", key=q)

# Navigation Buttons
col1, col2 = st.columns(2)
with col1:
    if st.button("Previous"):
        # Logic to go to previous question
        pass
with col2:
    if st.button("Next"):
        # Logic to go to next question and update progress
        st.session_state.progress += 20  # Update progress example
