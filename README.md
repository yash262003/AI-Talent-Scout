# **TalentScout AI Hiring Assistant – Project Document**

---

## **1. Project Title**
TalentScout AI Hiring Assistant – An AI-powered chatbot for candidate evaluation.

---

## **2. Objective**
The TalentScout AI Hiring Assistant is designed to streamline the candidate evaluation process by:
- Gathering candidate information such as name, contact details, experience, desired position, and tech stack.  
- Generating tailored technical questions based on the candidate’s declared tech stack.  
- Providing an interactive conversation experience with fallback handling for unexpected inputs.  
- Displaying candidate details along with the generated questions in a structured format.  
- Ending the conversation with a closing message and next steps.

---

## **3. Scope**

### **Core Functionalities**
- **User Interface (UI):**  
   - Built using Streamlit for a clean and interactive web-based application.  
- **Candidate Information Collection:**  
   - Captures key details: Name, Email, Phone, Experience, Desired Position, Location, and Tech Stack.  
- **Technical Question Generation:**  
   - Uses Google Gemini 2.0 Flash API to generate 3-5 technical questions based on the candidate’s tech stack.  
- **Context Handling:**  
   - Maintains conversation coherence with fallback responses for unexpected inputs.  
- **Error and Fallback Handling:**  
   - Provides meaningful responses when the chatbot fails to understand the input.  
- **Deployment:**  
   - Hosted on Hugging Face Spaces, making it accessible online.

---

## **4. Architecture**

### **System Architecture Overview**

The chatbot architecture consists of the following layers:
1. **User Interface Layer:**  
   - Streamlit-based web application where candidates interact with the chatbot.
2. **Chatbot Logic Layer:**  
   - Collects candidate details.  
   - Generates tailored technical questions.  
   - Handles fallback responses.  
3. **Google Gemini API Layer:**  
   - Generates technical questions based on the tech stack.  
4. **Hosting Platform:**  
   - Deployed on Hugging Face Spaces.  

---

## **5. Technical Stack**

### **Languages and Frameworks**
- **Python:** Core programming language for building the chatbot.  
- **Streamlit:** For creating the web-based user interface.  
- **Google Gemini API:** For generating AI-powered technical questions.  
- **Hugging Face Spaces:** For deployment and hosting.

### **Libraries and Dependencies**
- `streamlit`: For the web-based UI.  
- `google-generativeai`: For interacting with the Gemini API.  
- `python-dotenv`: For managing environment variables.  
- `os`: For accessing environment variables.  
- `pip`: For dependency management.  

---

## **6. Implementation Details**

### **Candidate Information Gathering**
The chatbot collects the following candidate details:
- Full Name  
- Email Address  
- Phone Number  
- Years of Experience  
- Desired Position(s)  
- Current Location  
- Tech Stack (e.g., Python, SQL, Django)

### **Technical Question Generation**
- Uses Google Gemini API to generate technical questions.  
- Based on the declared tech stack, the chatbot dynamically generates 3-5 questions tailored to the candidate's skills.  
- **Prompt Design:**  
   - "Generate 3-5 technical questions based on the following tech stack: {tech_stack}. Ensure the questions test proficiency in each technology."  
- This prompt ensures the questions are relevant and meaningful.

### **Fallback Handling**
- If the chatbot does not understand the input, it provides fallback responses such as:  
   - "I'm sorry, I didn't quite catch that. Could you rephrase?"  
   - "I'm here to help with candidate evaluation. Please provide tech stack details."  
   - "I'm only trained for hiring assistance. Let's continue with your details."  
- This ensures the chatbot stays on track.

### **End Conversation**
- The chatbot gracefully ends the conversation by thanking the candidate and indicating the next steps:  
   - "Thank you for using the TalentScout AI Hiring Assistant! We'll reach out to you with the next steps."

---

## **7. Deployment Process**

### **Hugging Face Deployment**
The chatbot is deployed on Hugging Face Spaces with the following steps:

1. **Project Structure:**
```
/app  
 ├── app.py                     # Streamlit application logic  
 ├── requirements.txt           # Python dependencies  
 ├── .env                       # Environment variables  
 ├── README.md                  # Project documentation  
 └── huggingface.yml            # Hugging Face configuration  
```

2. **Environment Configuration (`.env` file):**
```
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

3. **Hugging Face Configuration (`huggingface.yml` file):**
```yaml
sdk: streamlit  
app_file: app.py  
port: 7860  
```

4. **Running the App Locally**
- To run the app locally, use the following commands:
```
pip install -r requirements.txt  
streamlit run app.py  
```
- The app will be accessible at:  
   - Local: http://localhost:8501  
   - Network: http://<your-network-ip>:8501  

---

## **8. Challenges and Solutions**

### **Challenge 1: Missing Dependency Issues**
**Problem:**  
- Hugging Face Spaces failed to recognize the `google-generativeai` module, causing a `ModuleNotFoundError`.  

**Solution:**  
- Added `pip install google-generativeai` directly into `app.py` to ensure runtime installation.  
- Specified the package version `google-generativeai==0.4.0` in `requirements.txt` to avoid conflicts.

---

### **Challenge 2: Model Name Issues**
**Problem:**  
- Incorrect model name caused `404 model not found` errors.  

**Solution:**  
- Used the `genai.list_models()` method to verify the available models.  
- Correctly specified the `"gemini-2.0-flash"` model in the code.

---

### **Challenge 3: Caching Issues on Hugging Face**
**Problem:**  
- Hugging Face cached old dependencies, preventing the correct installation of `google-generativeai`.  

**Solution:**  
- Cleared the cache and restarted the Space.  
- Added `huggingface.yml` to force the environment to reinstall dependencies.

---

## **9. Future Enhancements**

### **1. Multi-Language Support**
- Add support for multiple languages to enhance accessibility for global candidates.

### **2. Improved Question Generation**
- Introduce dynamic question difficulty levels based on the candidate's experience.

### **3. Data Persistence**
- Store candidate responses in a database for future reference and analysis.

### **4. Integration with ATS**
- Automate the resume submission process by integrating with Applicant Tracking Systems (ATS).

---

## **10. Conclusion**
The **TalentScout AI Hiring Assistant** chatbot simplifies and enhances the candidate evaluation process by:
- Efficiently gathering candidate information.  
- Generating tailored technical questions based on the candidate’s tech stack.  
- Providing a seamless and interactive experience.  
- Deploying on Hugging Face Spaces for easy accessibility.  

This project demonstrates the practical application of **AI and NLP** in **streamlining recruitment workflows**.

---

✅ **Author:**  
**Navoday Yash Kaushal**  
AI/ML Enthusiast | Data Scientist | Full-Stack Developer
