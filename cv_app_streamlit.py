import streamlit as st
import json

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

# Dictionary to store responses
responses = {}

# Page navigation
st.title("Student CV Generator")
section = st.sidebar.selectbox("Select a Section to Fill", list(questions.keys()))

# Display questions for the selected section
st.header(section)
for q in questions[section]:
    response = st.text_input(q, key=f"{section}_{q}")
    responses[section] = responses.get(section, {})
    responses[section][q] = response

# Button to move to the next section
st.sidebar.write("Navigate through sections using this menu.")
if st.sidebar.button("Save Responses"):
    with open("student_cv_responses.json", "w") as file:
        json.dump(responses, file, indent=4)
    st.success("Your responses have been saved to 'student_cv_responses.json'.")

# "Boost Accuracy" suggestion area
st.sidebar.header("Boost Accuracy Tips")
if section in ["Work and Volunteer Experience", "Skills and Abilities"]:
    st.sidebar.write("Consider adding specific skills, roles, or tools relevant to your experience.")
