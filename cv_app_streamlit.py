import streamlit as st
import json

st.title("Student CV Questionnaire")

def main():
    st.header("Please fill out the following form to help us create your CV.")

    # Personal Information
    st.subheader("1. Personal Information and Contact Details")
    name = st.text_input("1. What is your full name?")
    contact_info = st.text_input("2. What is your primary contact information (phone number and email address)?")
    location = st.text_input("3. What is your current location (City, Postcode)?")
    online_profiles = st.text_input("4. Do you have any online professional profiles (LinkedIn, website, portfolio link)?")

    # Education and Academic Achievements
    st.subheader("2. Education and Academic Achievements")
    school = st.text_input("1. What school/college are you currently attending, and what year are you in?")
    subjects = st.text_input("2. What subjects are you studying, and do you have any grades or predicted grades?")
    awards = st.text_area("3. Have you received any awards or honours during your time in school (e.g., top student, subject awards)?")
    extracurriculars = st.text_area("4. Do you participate in any academic clubs, societies, or extracurricular academic activities?")

    # Work and Volunteer Experience
    st.subheader("3. Work and Volunteer Experience")
    work_experience = st.text_area("1. What paid work experiences have you had? Please provide job title, employer, and main responsibilities.")
    volunteer_experience = st.text_area("2. Have you volunteered or worked in any charity initiatives? Describe your role and what you contributed.")
    skills_learned = st.text_area("3. What specific skills or abilities have you developed through your work experiences?")
    proud_projects = st.text_area("4. Do you have any projects or accomplishments from these roles that you’re particularly proud of?")

    # Skills and Abilities
    st.subheader("4. Skills and Abilities")
    technical_skills = st.text_area("1. What are your strongest technical or practical skills (e.g., IT, communication, teamwork)?")
    soft_skills = st.text_area("2. Which personal attributes or soft skills (like leadership, organisation, creativity) would you say are your strengths?")
    other_skills = st.text_area("3. Are there any skills you have gained through hobbies, online learning, or personal projects?")
    skill_examples = st.text_area("4. Can you give an example of a skill you developed that has helped you perform better in other areas of life?")

    # Activities, Hobbies, and Interests
    st.subheader("5. Activities, Hobbies, and Interests")
    hobbies = st.text_area("1. What activities or hobbies do you enjoy outside of school and work?")
    groups = st.text_area("2. Have you been part of any clubs, sports teams, or creative groups?")
    hobby_achievements = st.text_area("3. Do you have any accomplishments or awards in these activities (e.g., sports medals, competition wins)?")
    hobby_skills = st.text_area("4. How have these interests helped you develop new skills or grow personally?")

    # Goals, Ambitions, and Motivations
    st.subheader("6. Goals, Ambitions, and Motivations")
    short_term_goals = st.text_area("1. What are your short-term goals for the next few years (e.g., work experience, higher education)?")
    career_aspirations = st.text_area("2. Are there any specific career fields, industries, or roles that you aspire to pursue?")
    motivations = st.text_area("3. What motivates you to succeed, both academically and personally?")
    future_skills = st.text_area("4. How do you see your current skills and experiences helping you achieve your future goals?")

    # Submit Button
    if st.button("Submit"):
        # Collect all responses into a dictionary
        responses = {
            "Personal Information": {
                "Full Name": name,
                "Contact Information": contact_info,
                "Location": location,
                "Online Profiles": online_profiles
            },
            "Education and Academic Achievements": {
                "School": school,
                "Subjects": subjects,
                "Awards": awards,
                "Extracurricular Activities": extracurriculars
            },
            "Work and Volunteer Experience": {
                "Work Experience": work_experience,
                "Volunteer Experience": volunteer_experience,
                "Skills Learned": skills_learned,
                "Proud Projects": proud_projects
            },
            "Skills and Abilities": {
                "Technical Skills": technical_skills,
                "Soft Skills": soft_skills,
                "Other Skills": other_skills,
                "Skill Examples": skill_examples
            },
            "Activities, Hobbies, and Interests": {
                "Hobbies": hobbies,
                "Groups": groups,
                "Hobby Achievements": hobby_achievements,
                "Hobby Skills": hobby_skills
            },
            "Goals, Ambitions, and Motivations": {
                "Short-term Goals": short_term_goals,
                "Career Aspirations": career_aspirations,
                "Motivations": motivations,
                "Future Skills": future_skills
            }
        }

        # Display a thank you message
        st.success("Thank you for submitting the form!")

        # Optionally, save the responses to a JSON file
        with open('responses.json', 'w') as f:
            json.dump(responses, f, indent=4)

        st.write("Your responses have been saved.")

if __name__ == "__main__":
    main()
