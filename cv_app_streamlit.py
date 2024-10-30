import streamlit as st
import json

# Apply light mode, larger font size, and increased padding
st.markdown(
    """
    <style>
    .reportview-container {
        background-color: #f8f9fa;
    }
    .main {
        color: #333333;
        font-size:22px;
    }
    .stTextInput > div > input {
        font-size: 20px !important;
        padding: 10px !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Define questions in sections
questions = {
    "Personal Information": [
        "What is your full name?",
        "What is your primary contact information (phone number and email address)?",
        "What is your current location (City, Postcode)?",
        "Do you have any online professional profiles (LinkedIn, website, portfolio link)?"
    ],
    "Education and Academic Achievements": [
        "What school/college are you currently attending, and what year are you in?",
        "What subjects are you studying, and do you have any grades or predicted grades?",
        "Have you received any awards or honours during your time in school?",
        "Do you participate in any academic clubs, societies, or extracurricular activities?"
    ],
    "Work and Volunteer Experience": [
        "What paid work experiences have you had?",
        "Have you volunteered or worked in any charity initiatives?",
        "What specific skills have you developed through these experiences?",
        "Any notable projects or accomplishments?"
    ],
    "Skills and Abilities": [
        "What are your strongest technical or practical skills?",
        "Which personal attributes or soft skills do you consider your strengths?",
        "Skills gained from hobbies or personal projects?",
        "An example of a skill that has helped you elsewhere?"
    ],
    "Activities, Hobbies, and Interests": [
        "What activities or hobbies do you enjoy outside of school and work?",
        "Any club memberships, sports teams, or creative groups?",
        "Accomplishments in these activities?",
        "How have these interests helped you grow personally?"
    ],
    "Goals, Ambitions, and Motivations": [
        "What are your short-term goals?",
        "Career fields or industries you aspire to pursue?",
        "What motivates you to succeed?",
        "How do you see your skills helping achieve future goals?"
    ]
}

# Initialize session state for navigation and responses
if "section_index" not in st.session_state:
    st.session_state.section_index = 0
if "question_index" not in st.session_state:
    st.session_state.question_index = 0
if "responses" not in st.session_state:
    st.session_state.responses = {}

sections = list(questions.keys())
current_section = sections[st.session_state.section_index]
current_question = questions[current_section][st.session_state.question_index]

# Display progress tracker with line breaks
st.sidebar.header("Progress Tracker")
for i, section in enumerate(sections):
    if i < st.session_state.section_index:
        st.sidebar.write(f"✅ {section}")
    elif i == st.session_state.section_index:
        st.sidebar.write(f"🔥 {section}")
    else:
        st.sidebar.write(f"⬜ {section}")

# Display "Boost Accuracy" tips
st.sidebar.header("Boost Accuracy Tips")
if current_section in ["Work and Volunteer Experience", "Skills and Abilities"]:
    st.sidebar.write("For this section, consider adding specific skills, tools, or relevant accomplishments.")
elif current_section == "Education and Academic Achievements":
    st.sidebar.write("Include grades, awards, and any extracurricular activities that relate to academic success.")

# Display current question with larger font size
st.title("Student CV Generator")
st.subheader(current_section)
st.markdown(f"<div style='font-size: 22px;'>{current_question}</div>", unsafe_allow_html=True)
response = st.text_input("", key=f"{current_section}_{current_question}")

# Store responses
st.session_state.responses[current_section] = st.session_state.responses.get(current_section, {})
st.session_state.responses[current_section][current_question] = response

# Navigation Buttons
col1, col2 = st.columns(2)
with col1:
    if st.button("Previous Question"):
        if st.session_state.question_index > 0:
            st.session_state.question_index -= 1
        elif st.session_state.section_index > 0:
            st.session_state.section_index -= 1
            st.session_state.question_index = len(questions[sections[st.session_state.section_index]]) - 1

with col2:
    if st.button("Next Question"):
        if st.session_state.question_index < len(questions[current_section]) - 1:
            st.session_state.question_index += 1
        elif st.session_state.section_index < len(sections) - 1:
            st.session_state.section_index += 1
            st.session_state.question_index = 0

# Save responses at the end of the questionnaire
if st.session_state.section_index == len(sections) - 1 and st.session_state.question_index == len(questions[current_section]) - 1:
    if st.button("Save Responses"):
        with open("student_cv_responses.json", "w") as file:
            json.dump(st.session_state.responses, file, indent=4)
        st.success("Your responses have been saved to 'student_cv_responses.json'.")
