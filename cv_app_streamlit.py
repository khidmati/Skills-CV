import streamlit as st
import json

# Load Material Design font and apply Google-like design with shadows and elevation
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap');

    .reportview-container {
        font-family: 'Roboto', sans-serif;
        background-color: #1e1e1e;  /* Slightly lighter background for better contrast */
    }

    .headline {
        font-size: 36px;
        color: #4285f4;  /* Google blue */
        font-weight: 700;
        text-align: center;
        margin-top: 20px;
        margin-bottom: 20px;
    }

    .title {
        font-size: 24px;
        color: #e0e0e0;
        font-weight: 500;
        text-align: left;
        margin-top: 10px;
        margin-bottom: 10px;
        padding-left: 20px;
    }

    .body-text {
        font-size: 20px;
        color: #e0e0e0;
        font-weight: 400;
        text-align: left;
        margin-bottom: 10px;
        padding-left: 20px;
    }

    .stTextInput > div > input {
        font-size: 18px !important;
        color: #ffffff;
        padding: 15px !important;
        background-color: #2a2a2a;
        border-radius: 8px;
        border: none;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        transition: box-shadow 0.3s ease;
    }

    .stTextInput > div > input:focus {
        box-shadow: 0 4px 12px rgba(66, 133, 244, 0.3);  /* Google blue shadow on focus */
        outline: none;
    }

    .stTextInput > div > input::placeholder {
        color: #b3b3b3; /* Subtle grey for placeholder */
    }

    .stButton > button {
        font-size: 18px;
        padding: 10px 20px;
        border-radius: 24px;
        background-color: #4285f4; /* Google blue */
        color: #fff;
        border: none;
        transition: background-color 0.3s, box-shadow 0.3s ease;
        box-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }

    .stButton > button:hover {
        background-color: #357ae8; /* Darker Google blue */
        box-shadow: 0 4px 8px rgba(0,0,0,0.3);
    }

    .progress-bar-container {
        width: 100%;
        background-color: #333;
        border-radius: 10px;
        overflow: hidden;
        height: 10px;
        margin-top: 20px;
        margin-bottom: 20px;
    }

    .progress-bar {
        height: 100%;
        width: {progress}%;
        background-color: #34a853;  /* Google green */
        transition: width 0.3s ease;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Define mode and questions
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

# Display progress bar with animation
progress_percentage = st.session_state.progress
st.markdown(
    f"<div class='progress-bar-container'><div class='progress-bar' style='width: {progress_percentage}%;'></div></div>",
    unsafe_allow_html=True
)
st.write(f"**Progress:** {progress_percentage}%")

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
        st.session_state.progress = max(0, st.session_state.progress - 20)  # Adjust progress backward
with col2:
    if st.button("Next"):
        # Logic to go to next question and update progress
        st.session_state.progress = min(100, st.session_state.progress + 20)  # Adjust progress forward
