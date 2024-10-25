import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv
from database import Database

# Page configuration must be the first Streamlit command
st.set_page_config(page_title="AI Parenting Assistant | AI育儿助手", page_icon="👶", layout="wide")

# Initialize database
db = Database()

# Load environment variables
load_dotenv()

# Set up OpenAI API key and Assistant ID
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ASSISTANT_ID = os.getenv("OPENAI_ASSISTANT_ID")

# Initialize session state
if 'user_id' not in st.session_state:
    st.session_state.user_id = None
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

def login_page():
    st.title("Welcome to AI Parenting Assistant")
    
    tab1, tab2 = st.tabs(["Login", "Register"])
    
    with tab1:
        with st.form("login_form"):
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            submit = st.form_submit_button("Login")
            
            if submit:
                user_id = db.verify_user(username, password)
                if user_id:
                    st.session_state.user_id = user_id
                    st.session_state.authenticated = True
                    st.success("Login successful!")
                    st.rerun()
                else:
                    st.error("Invalid username or password")
    
    with tab2:
        with st.form("register_form"):
            new_username = st.text_input("Choose Username")
            new_password = st.text_input("Choose Password", type="password")
            confirm_password = st.text_input("Confirm Password", type="password")
            email = st.text_input("Email")
            submit = st.form_submit_button("Register")
            
            if submit:
                if new_password != confirm_password:
                    st.error("Passwords do not match")
                elif len(new_password) < 6:
                    st.error("Password must be at least 6 characters long")
                else:
                    success, message = db.register_user(new_username, new_password, email)
                    if success:
                        st.success(message)
                        st.info("Please login with your new account")
                    else:
                        st.error(message)

def main_app():
    # Initialize OpenAI client
    client = OpenAI(api_key=OPENAI_API_KEY)

    # Your existing main app code here
    # [Previous app.py content goes here, starting from the custom CSS]
    # Make sure to keep all the functionality but remove the initial page_config
    # as it's already set at the top of the file

# Main app flow
if not st.session_state.authenticated:
    login_page()
else:
    # Add logout button in sidebar
    if st.sidebar.button("Logout"):
        st.session_state.authenticated = False
        st.session_state.user_id = None
        st.rerun()
    
    main_app()
