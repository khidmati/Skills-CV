import streamlit as st
import json

# Select Light Mode only with a clean, bright background
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap');

    /* General font settings */
    .reportview-container {
        font-family: 'Roboto', sans-serif;
        background-color: #ffffff; /* White background */
        color: #333333; /* Default dark grey for text */
    }
    .sidebar .sidebar-content {
        background-color: #f7f7f7; /* Light grey sidebar background */
    }

    /* Headline styling */
    .headline {
        font-size: 36px;
        color: #333333;  /* Dark grey */
        font-weight: 700;
        text-align: center;
        margin-top: 20px;
    }

    /* Section title styling */
    .title {
        font-size: 24px;
        color: #555555;  /* Medium grey */
        font-weight: 500;
        padding-left: 20px;
        margin-top: 10px;
        margin-bottom: 5px;
    }

    /* Body text styling */
    .body-text {
        font-size: 20px;
        color: #666666;  /* Lighter grey */
        padding-left: 20px;
        margin-bottom: 15px;
    }

    /* Input field styling */
    .stTextInput > div > input {
        font-size: 18px;
        color: #333333;  /* Darker grey for input text */
        background-color: #ffffff;  /* White background for input fields */
        border-radius: 5px;
        border: 1px solid #ddd;  /* Light grey border */
        padding: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);  /* Subtle shadow */
    }
    .stTextInput > div > input::placeholder {
        color: #999999; /* Subtle grey for placeholder text */
    }

    /* Button styling */
    .stButton > button {
        font-size: 18px;
        padding: 10px 20px;
        border-radius: 20px;
        background-color: #4285f4;  /* Google blue */
        color: #ffffff;
        border: none;
        transition: background-color 0.3s, box-shadow 0.3s;
    }
    .stButton > button:hover {
        background-color: #357ae8;
        box-shadow: 0 4px 8px rgba(0,0,0,0.15);
    }

    /* Progress bar styling */
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
        background-color: #34a853;  /* Google green for progress */
        transition: width 0.3s ease;
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
        if st.session_state
