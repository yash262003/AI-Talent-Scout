import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv("YOUR_API_KEY")

# Configure Gemini API
genai.configure(api_key=GEMINI_API_KEY)

# Streamlit UI
st.set_page_config(page_title="TalentScout AI Hiring Assistant")
st.header("TalentScout")

# Greeting message
st.write("### 🤖 Hello! Welcome to the TalentScout AI Hiring Assistant")
st.write("I will help you by gathering your details and generating technical questions based on your tech stack.")

# Candidate Info Form
with st.form(key='candidate_form'):
    name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    phone = st.text_input("Phone Number")
    experience = st.slider("Years of Experience", 0, 20, 2)
    position = st.text_input("Desired Position(s)")
    location = st.text_input("Current Location")
    tech_stack = st.text_area("Tech Stack (comma-separated, e.g., Python, SQL, Django)")
    submit = st.form_submit_button("Submit your details")

# Gemini response function
def get_gemini_response(question):
    try:
        model = genai.GenerativeModel("gemini-2.0-flash")  # Use latest Gemini model
        response = model.generate_content(question)
        if response and hasattr(response, "text"):
            return response.text
        else:
            return "No valid response received."
    except Exception as e:
        return f"Error: {str(e)}"

# Context handling
def handle_fallback(input_text):
    fallback_responses = [
        "I'm sorry, I didn't quite catch that. Could you rephrase?",
        "I'm here to help with candidate evaluation. Please provide tech stack details.",
        "I'm only trained for hiring assistance. Let's continue with your details."
    ]
    return fallback_responses[0]

# Display results
if submit:
    if name and email and phone and tech_stack.strip():
        st.write("### Candidate Details")
        st.write(f"**Name:** {name}")
        st.write(f"**Email:** {email}")
        st.write(f"**Phone:** {phone}")
        st.write(f"**Experience:** {experience} years")
        st.write(f"**Position:** {position}")
        st.write(f"**Location:** {location}")
        st.write(f"**Tech Stack:** {tech_stack}")
        
        # Generate technical questions
        prompt = f"Generate 3-5 technical questions based on the following tech stack: {tech_stack}. Ensure the questions test proficiency in each technology."
        response = get_gemini_response(prompt)
        
        # Fallback handling
        if "Error" in response or "No valid response received" in response:
            response = handle_fallback(response)
        
        st.write("### Technical Questions")
        st.write(response)
        
        # End conversation
        st.success("Thank you for using the TalentScout AI Hiring Assistant! We'll reach out to you with the next steps.")
    else:
        st.warning("Please fill out all required fields.")
