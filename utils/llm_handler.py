from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from utils.configuration import get_llm
import streamlit as st


def compare_resume(resume_text:str, job_post_text:str)->str:
    try:
        resume_compare_prompt_template="""
        Compare the following resume with the job description provided below. 
        Identify the key skills, qualifications, and experiences in the resume that match the job description. 
        Additionally, highlight any gaps or missing requirements from the resume and suggest improvements or 
        specific wording adjustments to better align with the job description. 
        Provide a compatibility score out of 100 based on how well the resume matches the job description, 
        and recommend specific areas for optimization.

        Resume : {RESUME_TEXT}
        Job Description : {JOB_POST_TEXT}
        """
        
        resume_compare_prompt=ChatPromptTemplate.from_template(resume_compare_prompt_template)
        
        llm=get_llm()
        
        resume_compare_chain=(
            {"RESUME_TEXT":RunnablePassthrough(), "JOB_POST_TEXT":RunnablePassthrough()} |
            resume_compare_prompt |
            llm |
            StrOutputParser()
        )
        
        resume_comparison=resume_compare_chain.invoke({"RESUME_TEXT":resume_text, "JOB_POST_TEXT":job_post_text})
        
        return resume_comparison

    except Exception as e:
        st.error("Error: " + str(e.args))