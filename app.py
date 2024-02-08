from dotenv import load_dotenv

load_dotenv()

import os
import streamlit as st
from PIL import Image
import PyPDF2 as pdf
import google.generativeai as genai
import io, base64


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_repsonse(input):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content(input)
    return response.text

def input_pdf_text(uploaded_file):
    reader=pdf.PdfReader(uploaded_file)
    text=""
    for page in range(len(reader.pages)):
        page=reader.pages[page]
        text+=str(page.extract_text())
    return text

input_promt ="""
Hey Act Like a skilled or very experience ATS(Application Tracking System)
with a deep understanding of tech field,software engineering,data science ,data analyst
and big data engineer. Your task is to evaluate the resume based on the given job description.
You must consider the job market is very competitive and you should provide 
best assistance for improving the resumes. Assign the percentage Matching based 
on Jd and the missing keywords with high accuracy
resume:{text}
description:{jd}

I want the response in one single string having the structure 
["JD Match":"%",Experience Match:"", "MissingKeywords:[]","Profile Summary":""]
"""

#streamlit app

st.set_page_config(page_title="ATS resume Helper")
st.header("ATS Tracking System")
jd =st.text_area("Job Description: ",key="input")
uploaded_file = st.file_uploader("Upload your Resume (PDF)...",type=["pdf"])
submit = st.button("Matching score🙃")



# submit1 = st.button("Tell Me about the Resume📃")
# submit2 = st.button("How can i Improviise my skills✨")
# submit3 = st.button("What are the keywords that are missing in my resume🧲")

if submit:
    if uploaded_file is not None and jd: 
        text = input_pdf_text(uploaded_file=uploaded_file)        
        response =get_gemini_repsonse(input_promt)
        st.subheader(response)




