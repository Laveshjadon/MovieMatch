import google.generativeai as genai
import streamlit as st
import time

chat_session = None

def get_gemini_key():
    try:
        return st.secrets["GEMINI_API_KEY"]
    except KeyError:
        return None

def set_api_key():
    api_key = get_gemini_key()
    if not api_key:
        return None
    genai.configure(api_key=api_key)
    return genai.GenerativeModel('gemini-1.5-flash')

def ask_gpt(prompt):
    global chat_session
    try:
        model = set_api_key()
        if not model:
            return "Error: GEMINI_API_KEY not found in .streamlit/secrets.toml"
            
        if chat_session is None:
            chat_session = model.start_chat(history=[])
            print("Gemini chat session initialized")
            
        response = chat_session.send_message(prompt)
        print("Run completed")
        print(response.text)
        return response.text
        
    except Exception as e:
        return f"An error occurred: {str(e)}"
