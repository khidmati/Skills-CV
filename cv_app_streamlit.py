import streamlit as st
import json

# Define the questions in a structured format
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
        "What paid work experiences have you had? Please provide job title, employer, and main responsibilities.",
        "Have you volunteered or worked in any charity initiatives? Describe your role and what you contributed.",
        "What specific skills or abilities have you developed through your work experiences?",
        "Do you have any projects or accomplishments from these roles that you’re particularly proud of?"
    ],
    "Skills and Abilities": [
        "What are your strongest technical or practical skills?",
        "Which personal attributes or soft skills do you consider your strengths?",
        "Are there any skills you have gained through hobbies, online learning, or personal projects?",
        "Can you give an example of a skill you developed that has helped you perform better in other areas of life?"
    ],
    "Activities, Hobbies, and Interests": [
        "What activities or hobbies do you enjoy outside of school and work?",
        "Have you been part of any clubs, sports teams, or creative groups?",
        "Do you have any accomplishments or awards in these activities?",
        "How have these interests helped you grow personally?"
    ],
    "Goals, Ambitions, and Motivations": [
        "What are your short-term goals for the next few years?",
        "Are there any specific career fields, industries, or roles you aspire to pursue?",
        "What motivates you to succeed?",
        "How do you see your current skills and experiences helping you achieve your future goals?"
    ]
}

# Dictionary to store responses
responses = {}

# Streamlit UI for each category and question
st.title("Student CV Generator")

# Loop through each category and question
for category, qs in questions.items():
    st.header(category)
    responses[category] = {}
    
    for q in qs:
        response = st.text_input(q, key=f"{category}_{q}")
        responses[category][q] = response

# Button to save responses to a JSON file
if st.button("Save Responses"):
    with open("student_cv_responses.json", "w") as file:
        json.dump(responses, file, indent=4)
    st.success("Your responses have been saved to 'student_cv_responses.json'.")
