import streamlit as st
import json

# Set page configuration
st.set_page_config(
    page_title="Student CV Questionnaire",
    page_icon=":memo:",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Custom CSS for styling
st.markdown("""
    <style>
    /* Import Poppins font from Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Poppins&display=swap');

    /* Set font family and increase font size */
    html, body, [class*="css"]  {
        font-family: 'Poppins', sans-serif;
        font-size: 20px; /* Increase base font size */
    }

    /* Increase header sizes */
    h1 {
        font-size: 3em !important;
    }
    h2 {
        font-size: 2.5em !important;
    }
    h3 {
        font-size: 2em !important;
    }

    /* Style the progress bar */
    .stProgress > div > div > div > div {
        background-color: #4CAF50;
    }

    /* Light background color */
    body {
        background-color: #f5f5f5;
    }

    /* Style the Next button */
    .stButton > button {
        font-size: 1.2em;
        padding: 10px 20px;
    }
    </style>
    """, unsafe_allow_html=True)

def main():
    st.title("Student CV Questionnaire")

    # Initialize session state variables
    if 'question_number' not in st.session_state:
        st.session_state.question_number = 0
    if 'responses' not in st.session_state:
        st.session_state.responses = {}
    if 'questions' not in st.session_state:
        st.session_state.questions = get_questions()
    if 'total_questions' not in st.session_state:
        st.session_state.total_questions = sum(len(section['questions']) for section in st.session_state.questions)

    # Display progress bar
    progress = st.session_state.question_number / st.session_state.total_questions
    st.progress(progress)

    # Get current question indices
    current_section_index, current_question_index = get_current_question_indices()
    if current_section_index is not None and current_question_index is not None:
        current_section = st.session_state.questions[current_section_index]
        current_question = current_section['questions'][current_question_index]

        # Display section header if it's the first question in the section
        if current_question_index == 0:
            st.header(current_section['header'])

        # Display the question
        st.subheader(current_question['question'])
        answer = st.text_area("", key=f"q{st.session_state.question_number}")

        # Next button
        if st.button("Next"):
            # Save the answer
            save_answer(current_section['section'], current_question['key'], answer)
            # Move to the next question
            st.session_state.question_number += 1
            # Clear the text area by rerunning the app without calling st.experimental_rerun()
            st.experimental_set_query_params(run=str(st.session_state.question_number))
            st._rerun()

    else:
        # All questions have been answered
        st.success("Thank you for completing the questionnaire!")

        # Optionally, save the responses to a JSON file
        with open('responses.json', 'w') as f:
            json.dump(st.session_state.responses, f, indent=4)

        st.write("Your responses have been saved.")

def get_questions():
    # Define all questions in a structured format
    return [
        {
            'section': 'Personal Information',
            'header': '1. Personal Information and Contact Details',
            'questions': [
                {'key': 'Full Name', 'question': 'What is your full name?'},
                {'key': 'Contact Information', 'question': 'What is your primary contact information (phone number and email address)?'},
                {'key': 'Location', 'question': 'What is your current location (City, Postcode)?'},
                {'key': 'Online Profiles', 'question': 'Do you have any online professional profiles (LinkedIn, website, portfolio link)?'}
            ]
        },
        {
            'section': 'Education and Academic Achievements',
            'header': '2. Education and Academic Achievements',
            'questions': [
                {'key': 'School', 'question': 'What school/college are you currently attending, and what year are you in?'},
                {'key': 'Subjects', 'question': 'What subjects are you studying, and do you have any grades or predicted grades?'},
                {'key': 'Awards', 'question': 'Have you received any awards or honours during your time in school (e.g., top student, subject awards)?'},
                {'key': 'Extracurricular Activities', 'question': 'Do you participate in any academic clubs, societies, or extracurricular academic activities?'}
            ]
        },
        {
            'section': 'Work and Volunteer Experience',
            'header': '3. Work and Volunteer Experience',
            'questions': [
                {'key': 'Work Experience', 'question': 'What paid work experiences have you had? Please provide job title, employer, and main responsibilities.'},
                {'key': 'Volunteer Experience', 'question': 'Have you volunteered or worked in any charity initiatives? Describe your role and what you contributed.'},
                {'key': 'Skills Learned', 'question': 'What specific skills or abilities have you developed through your work experiences?'},
                {'key': 'Proud Projects', 'question': 'Do you have any projects or accomplishments from these roles that you’re particularly proud of?'}
            ]
        },
        {
            'section': 'Skills and Abilities',
            'header': '4. Skills and Abilities',
            'questions': [
                {'key': 'Technical Skills', 'question': 'What are your strongest technical or practical skills (e.g., IT, communication, teamwork)?'},
                {'key': 'Soft Skills', 'question': 'Which personal attributes or soft skills (like leadership, organisation, creativity) would you say are your strengths?'},
                {'key': 'Other Skills', 'question': 'Are there any skills you have gained through hobbies, online learning, or personal projects?'},
                {'key': 'Skill Examples', 'question': 'Can you give an example of a skill you developed that has helped you perform better in other areas of life?'}
            ]
        },
        {
            'section': 'Activities, Hobbies, and Interests',
            'header': '5. Activities, Hobbies, and Interests',
            'questions': [
                {'key': 'Hobbies', 'question': 'What activities or hobbies do you enjoy outside of school and work?'},
                {'key': 'Groups', 'question': 'Have you been part of any clubs, sports teams, or creative groups?'},
                {'key': 'Hobby Achievements', 'question': 'Do you have any accomplishments or awards in these activities (e.g., sports medals, competition wins)?'},
                {'key': 'Hobby Skills', 'question': 'How have these interests helped you develop new skills or grow personally?'}
            ]
        },
        {
            'section': 'Goals, Ambitions, and Motivations',
            'header': '6. Goals, Ambitions, and Motivations',
            'questions': [
                {'key': 'Short-term Goals', 'question': 'What are your short-term goals for the next few years (e.g., work experience, higher education)?'},
                {'key': 'Career Aspirations', 'question': 'Are there any specific career fields, industries, or roles that you aspire to pursue?'},
                {'key': 'Motivations', 'question': 'What motivates you to succeed, both academically and personally?'},
                {'key': 'Future Skills', 'question': 'How do you see your current skills and experiences helping you achieve your future goals?'}
            ]
        },
        {
            'section': 'Experiences and Personal Reflections',
            'header': '7. Experiences and Personal Reflections',
            'questions': [
                {'key': 'Helping Others', 'question': 'Who have you helped in the past week, month, or year? What did you do for them?'},
                {'key': 'Problem Solving', 'question': 'Describe a time when you solved a problem for someone else. What steps did you take?'},
                {'key': 'Overcoming Challenges', 'question': 'Think about a recent challenge you faced. How did you overcome it?'},
                {'key': 'Organizational Roles', 'question': 'Have you organized or participated in any events or activities? What was your role?'},
                {'key': 'Daily Responsibilities', 'question': 'What are some tasks you regularly handle at home or school? How do you manage them?'},
                {'key': 'Learning Experiences', 'question': 'Have you learned something new recently? How did you approach the learning process?'}
            ]
        }
    ]

def get_current_question_indices():
    # Calculate current section and question indices based on question_number
    q_num = st.session_state.question_number
    total = 0
    for i, section in enumerate(st.session_state.questions):
        num_questions = len(section['questions'])
        if total + num_questions > q_num:
            question_index = q_num - total
            return i, question_index
        total += num_questions
    return None, None

def save_answer(section, key, answer):
    # Save the answer in the session state responses
    if section not in st.session_state.responses:
        st.session_state.responses[section] = {}
    st.session_state.responses[section][key] = answer

if __name__ == "__main__":
    main()
