from langchain_community.document_loaders import WebBaseLoader
import streamlit as st

def get_job_posts(post_url:str, job_description:str)->str:
    try:
        if post_url!="":
            job_post_text=WebBaseLoader(post_url).load()
            return job_post_text
        else:
            return job_description

    except Exception as e:
        st.error("Error: " + str(e.args))
    