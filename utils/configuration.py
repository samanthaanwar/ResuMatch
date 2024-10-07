import os
import yaml
from langchain_groq.chat_models import ChatGroq
import streamlit as st

with open("utils/config.yaml") as file:
    config = yaml.safe_load(file)
    
os.environ['GROQ_API_KEY']=st.secrets['GROQ_API_KEY']

def get_llm():
    return ChatGroq(model=config["llm"]["model"],
                          temperature=config["llm"]["temperature"],
                            max_tokens=None,
                            timeout=None)
    


