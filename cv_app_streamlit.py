import streamlit as st
import json

# Add a toggle for Day/Night Mode
mode = st.sidebar.radio("Select Mode", ["Light Mode", "Dark Mode"])

# Apply custom CSS for distinct Light and Dark modes with improved colours and font hierarchy
if mode == "Light Mode":
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap');
        
        .reportview-container {
            font-family: 'Roboto', sans-serif;
            background-color: #ffffff;  /* True white background */
            color: #1a1a1a;
        }
        .sidebar .sidebar-content {
            background-color: #f8f8f8; /* Very light grey for sidebar */
        }
        .headline {
            font-size: 48px;
            color: #4285f4;  /* Google blue */
            font-weight: 700;
            text-align: center;
            margin-top: 20px;
            margin-bottom: 20px;
        }
        .title {
            font-size: 28px;
            color: #333333;
            font-weight: 500;
            text-align: left;
            margin-top: 10px;
            margin-bottom: 10px;
            padding-left: 20px;
        }
        .body-text {
            font-size: 22px;
            color: #555555;
            font-weight: 400;
            text-align: left;
            margin-bottom: 10px;
            padding-left: 20px;
        }
        .stTextInput > div > input {
            font-size: 20px !important;
            color: #333333;
            padding: 15px !important;
            background-color: #ffffff;
            border-radius: 8px;
            border: 1px solid #ddd;  /* Light grey border */
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        }
        .stTextInput > div > input::placeholder {
            color: #888888;
        }
        .stButton > button {
            font-size: 20px;
            padding: 10px 20px;
            border-radius: 24px;
            background-color: #4285f4;  /* Google blue */
            color: #ffffff;
            border: none;
            transition: background-color 0.3s, box-shadow 0.3s;
            box-shadow: 0 2px 4px rgba(0,0,0,0.15);
        }
        .stButton > button:hover {
            background-color: #357ae8;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        }
        .progress-bar-container {
            width: 100%;
            background-color: #e0e0e0;
            border-radius: 10px;
            overflow: hidden;
            height: 12px;
            margin-top: 20px;
            margin-bottom: 20px;
        }
        .progress-bar {
            height: 100%;
            background-color: #34a853;  /* Google green */
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
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap');

        .reportview-container {
            font-family: 'Roboto', sans-serif;
            background-color: #1e1e1e;
            color: #ffffff;
        }
        .headline {
            font-size: 48px;
            color: #ffcc00;  /* Google yellow for dark mode */
            font-weight: 700;
            text-align: center;
            margin-top: 20px;
            margin-bottom: 20px;
        }
        .title {
            font-size: 28px;
            color: #e0e0e0;
            font-weight: 500;
            text-align: left;
            margin-top: 10px;
            margin-bottom: 10px;
            padding-left: 20px;
        }
        .body-text {
            font-size: 22px;
            color: #bbbbbb;
            font-weight: 400;
            text-align: left;
            margin-bottom: 10px;
            padding-left: 20px;
        }
        .stTextInput > div > input {
            font-size: 20px !important;
            color: #ffffff;
            padding: 15px !important;
            background-color: #2a2a2a;
            border-radius: 8px;
            border: none;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .stButton > button {
            font-size: 20px;
            padding: 10px 20px;
            border-radius: 24px;
            background-color: #4285f4;
            color: #ffffff;
            border: none;
            transition: background-color 0.3s, box-shadow 0.3s;
            box-shadow: 0 2px 4px rgba(0,0,0,0.15);
        }
        .progress-bar-container {
            width: 100%;
            background-color: #333;
            border-radius: 10px;
            height: 12px;
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

# Change header title to "FREE CV"
st.markdown("<div class='headline'>FREE CV</div>", unsafe_allow_html=True)

# Example progress tracking
if "progress" not in st.session_state:
    st.session_state.progress = 0
progress_percentage = st.session_state.progress

# Display progress bar
st.markdown(
    f"<div class='progress-bar-container'><div class='progress-bar' style='width: {progress_percentage}%;'></div></div>",
    unsafe_allow_html=True
)
st.write(f"**Progress:** {progress_percentage}%")

# Define some sample sections and questions
questions = {
    "Personal Information": [
        "What is your full name?",
        "What is your primary contact information (phone number and email address)?"
    ]
}

# Display sections and input fields
for section, qs in questions.items():
    st.markdown(f"<div class='title'>{section}</div>", unsafe_allow_html=True)
    for q in qs:
        st.markdown(f"<div class='body-text'>{q}</div>", unsafe_allow_html=True)
        st.text_input("", key=q)

# Example navigation buttons with updated styles
col1, col2 = st.columns(2)
with col1:
    if st.button("Previous"):
        st.session_state.progress = max(0, st.session_state.progress - 20)
with col2:
    if st.button("Next"):
        st.session_state.progress = min(100, st.session_state.progress + 20)
