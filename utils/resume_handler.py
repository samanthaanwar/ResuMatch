import os
from langchain.document_loaders import TextLoader, PyPDFLoader, Docx2txtLoader
from tempfile import TemporaryDirectory
import streamlit as st

def get_resume_text(uploaded_file:str)->str:
    try:
        tmp_dir = "temp"
        
        temp_file_path=os.path.join(tmp_dir, uploaded_file.name)
            
        with open(temp_file_path, "wb") as resume_file:
            resume_file.write(uploaded_file.read())
                
        upload_document_extension=os.path.splitext(uploaded_file.name)[1]
        
        if upload_document_extension==".pdf":
            loader=PyPDFLoader(temp_file_path)
        if upload_document_extension==".docx":
            loader=Docx2txtLoader(temp_file_path)
        if upload_document_extension==".txt":
            loader=TextLoader(temp_file_path)
            
        if loader:
            resume_text=loader.load()
            
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)

            return resume_text
        
    except Exception as e:
        st.error("Error: " + str(e.args))
