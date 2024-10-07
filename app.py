import streamlit as st
from utils.job_post_handler import get_job_posts
from utils.resume_handler import get_resume_text
from utils.llm_handler import compare_resume

# App title
st.set_page_config(page_title="📝 ResuMatchAI 🌐")

st.title("📝 ResuMatchAI! 🌐")
st.write("-----------------------------------------------------------------------------------------------------------") 
st.write("📝 ResuMatchAI 🌐 – the ultimate AI-powered tool for job seekers looking to enhance their resumes and match them seamlessly with job descriptions. Using advanced Language Learning Models (LLMs) and LangChain technology, ResuMatchAI analyzes your resume and compares it with your target job descriptions, identifying strengths, gaps, and areas for improvement. Get personalized suggestions, optimized keywords, and actionable insights to ensure your CV stands out to recruiters and passes Applicant Tracking Systems (ATS) with ease. Take your job application game to the next level with ResuMatchAI – where your dream job is just a match away!🌟")
st.write("-----------------------------------------------------------------------------------------------------------") 


uploaded_resume = st.file_uploader("Upload a resume in formats like PDF, Word, or text :", accept_multiple_files=False)


job_post_url=st.text_input("Paste the URL of the job posting here (optional) : ", value="")

st.write("or")

job_post_description=st.text_area("Paste the job posting description here (optional) : ", value="")


if uploaded_resume is not None:
    if st.button("Compare"):
        with st.spinner("Thinking..."):
            resume_text=get_resume_text(uploaded_file=uploaded_resume)
            
            job_description=get_job_posts(post_url=job_post_url, job_description=job_post_description)
            
            resume_comparison=compare_resume(resume_text=resume_text, job_post_text=job_description)
            
            st.write(resume_comparison)