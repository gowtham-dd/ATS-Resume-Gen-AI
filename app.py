from dotenv import load_dotenv

load_dotenv()
import io
import base64
import streamlit as st
import os
from PIL import Image
import pdf2image
import google.generativeai as genai
import fitz  # PyMuPDF


genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

def get_gemini_response(prompt, pdf_text, user_input):
    model = genai.GenerativeModel('gemini-2.5-pro')
    response = model.generate_content([prompt, pdf_text, user_input])
    return response.text



def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        pdf_doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
        text_content = pdf_doc[0].get_text("text")  # only first page
        return text_content  # send as plain string
    else:
        raise FileNotFoundError("No file uploaded")


## Streamlit app
st.set_page_config(page_title="ATS RESUME EXPERT")
st.header("ATS Tracking System")
input_text=st.text_area("Job Description:",key="input")
uploaded_file=st.file_uploader("Upload your resume (PDF)...",type=["pdf"])


if uploaded_file is not None:
    st.write("PDF Uploaded Succesfully")


submit1= st.button("Tell me about the Resume")
submit2= st.button("How can i improvise mt skills ")
submit3= st.button("Percentage Match")

input_promt1="""
You are an expert Applicant Tracking System (ATS) and HR recruiter. 
I will provide you with a candidate’s resume. 
Your task is to:
1. Review the provided resume against the job description for these profiles.
2. Summarize the candidate’s background, experience, education, and skills.
3. Highlight their key strengths and unique value.
4. Point out any gaps, weaknesses, or improvements needed.
5. Rate overall job readiness on a scale of 1–10.

"""

input_promt2="""
You are an expert career coach and ATS system. 
I will provide you with a candidate’s resume. 
Your task is to:
1. Identify the candidate’s current skills (technical, soft, and domain-specific).
2. Highlight which of these skills are strong and market-ready.
3. Identify missing or weak skills that limit the candidate’s career growth.
4. Suggest specific skills, certifications, tools, or knowledge areas they should learn.
5. Recommend practical ways to build these skills (online courses, projects, internships, networking, workshops, etc.).
6. Provide a short roadmap (immediate, short-term, and long-term improvements).

"""

input_promt3="""
You are an advanced ATS system. 
I will provide you with a candidate’s resume and a job description. 

Your task is to:
1. Compare the resume with the job description.
2. Identify skills, qualifications, and experience that match.
3. Highlight missing or weak areas.
4. Give a percentage match score (0–100%) that reflects how well the resume fits the job.
5. Provide a short explanation for the score.

"""


if submit1:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_promt1,pdf_content,input_text)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload the resume")


elif submit2:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_promt2,pdf_content,input_text)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload the resume")



elif submit3:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_promt3,pdf_content,input_text)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload the resume")


