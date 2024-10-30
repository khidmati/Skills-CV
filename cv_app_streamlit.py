import streamlit as st
import json

# Toggle between Light and Dark mode
mode = st.sidebar.radio("Select Mode", ["Light Mode", "Dark Mode"])

# Simplified CSS for Light and Dark Mode with minimal changes
if mode == "Light Mode":
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap');
        
        .reportview-container {
            font-family: 'Roboto', sans-serif;
            background-color: #ffffff;
            color: #000000;
        }
        .sidebar .sidebar-content {
            background-color: #f8f8f8;
        }
        .headline {
            font-size: 36px;
            color: #4285f4;
            font-weight: 700;
            text-align: center;
            margin-top: 20px;
        }
        .title {
            font-size: 24px;
            color: #333333;
            font-weight: 500;
            padding-left: 20px;
            margin-top: 10px;
            margin-bottom: 5px;
        }
        .body-text {
            font-size: 20px;
            color: #666666;
            padding-left: 20px;
            margin-bottom: 15px;
        }
        .stTextInput > div > input {
            font-size: 18px;
            color: #333333;
            background-color: #f7f7f7;
            border-radius: 5px;
            border: 1px solid #ccc;
            padding: 10px;
        }
        .stButton > button {
            font-size: 18px;
            padding: 10px 20px;
            border-radius: 20px;
            background-color: #4285f4;
            color: #ffffff;
            border: none;
        }
        .progress-bar-container {
            width: 100%;
            background-color: #e0e0e0;
            border-radius: 10px;
            overflow: hidden;
            height: 10px;
            margin-top: 20px;
            margin-bottom: 20px;
        }
        .progress-bar {
            height: 100%;
            background-color: #34a853;
            transition: width 0.3s ease;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
else:
    st.markdown(
        """
        <style>
        .reportview-container {
            background-color: #1e1e1e;
            color: #ffffff;
        }
        .headline {
            font-size: 36px;
            color: #ffcc00;
            font-weight: 700;
            text-align: center;
        }
        .title {
            font-size: 24px;
            color: #e0e0e0;
            padding-left: 20px;
        }
        .body-text {
            font-size: 20px;
            color: #bbbbbb;
            padding-left: 20px;
        }
        .stTextInput > div > input {
            background-color: #333333;
            color: #ffffff;
        }
        .stButton > button {
            background-color: #4285f4;
            color: #ffffff;
        }
        .progress-bar-container {
            background-color: #333;
        }
        .progress-bar {
            background-color: #34a853;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Title and headline
st.markdown("<div class='headline'>FREE CV</div>", unsafe_allow_html=True)

# Questions and Progress Setup
questions = {
    "Personal Information": [
        "What is your full name?",
        "What is your primary contact information (phone number and email address)?",
        "What is your current location (City, Postcode)?"
    ],
    # You can add more sections and questions here
}

# Initialize session state for progress tracking
if "responses" not in st.session_state:
    st.session_state.responses = {section: {} for section in questions}
if "current_section_index" not in st.session_state:
    st.session_state.current_section_index = 0
if "current_question_index" not in st.session_state:
    st.session_state.current_question_index = 0

# Calculate progress
total_questions = sum(len(qs) for qs in questions.values())
answered_questions = sum(
    1 for section in st.session_state.responses for answer in st.session_state.responses[section].values() if answer
)
progress_percentage = int((answered_questions / total_questions) * 100)

# Display progress bar
st.markdown(
    f"<div class='progress-bar-container'><div class='progress-bar' style='width: {progress_percentage}%;'></div></div>",
    unsafe_allow_html=True
)
st.write(f"**Progress:** {progress_percentage}%")

# Display current question
sections = list(questions.keys())
current_section = sections[st.session_state.current_section_index]
current_question = questions[current_section][st.session_state.current_question_index]

# Display current section and question
st.markdown(f"<div class='title'>{current_section}</div>", unsafe_allow_html=True)
st.markdown(f"<div class='body-text'>{current_question}</div>", unsafe_allow_html=True)
response = st.text_input("", key=f"{current_section}_{current_question}")

# Store the response
st.session_state.responses[current_section][current_question] = response

# Navigation logic
col1, col2 = st.columns(2)
with col1:
    if st.button("Previous"):
        if st.session_state.current_question_index > 0:
            st.session_state.current_question_index -= 1
        elif st.session_state.current_section_index > 0:
            st.session_state.current_section_index -= 1
            st.session_state.current_question_index = len(questions[sections[st.session_state.current_section_index]]) - 1

with col2:
    if st.button("Next"):
        if st.session_state.current_question_index < len(questions[current_section]) - 1:
            st.session_state.current_question_index += 1
        elif st.session_state.current_section_index < len(sections) - 1:
            st.session_state.current_section_index += 1
            st.session_state.current_question_index = 0
