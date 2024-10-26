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

# Initialize OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "thread_id" not in st.session_state:
    st.session_state.thread_id = client.beta.threads.create().id
if "user_info" not in st.session_state:
    st.session_state.user_info = {}
if "show_chat" not in st.session_state:
    st.session_state.show_chat = False
if "user_id" not in st.session_state:
    st.session_state.user_id = None
if "language" not in st.session_state:
    st.session_state.language = "en"

# Custom CSS (your existing CSS here)
st.markdown("""
<style>
    .stApp {
        background-color: #f0f8ff;
    }
    .stTextInput > div > div > input {
        background-color: #ffffff;
    }
    .stSelectbox > div > div > select {
        background-color: #ffffff;
    }
    .stButton > button {
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
    }
    .stButton > button:hover {
        background-color: #45a049;
    }
    .chat-message {
        padding: 1.5rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
        display: flex;
        flex-direction: column;
    }
    .chat-message.user {
        background-color: #2b313e;
        color: #ffffff;
        align-self: flex-end;
    }
    .chat-message.assistant {
        background-color: #ffffff;
        color: #000000;
        align-self: flex-start;
    }
    .chat-message .message {
        margin-bottom: 0;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar for language selection and user authentication
with st.sidebar:
    # Language selector
    st.selectbox(
        "Language | 语言",
        ["English", "中文"],
        key="lang_select",
        on_change=lambda: setattr(st.session_state, "language", "en" if st.session_state.lang_select == "English" else "zh")
    )
    
    st.divider()
    
    # User authentication section
    if st.session_state.user_id is None:
        auth_option = st.radio("Choose an option:", ["Login", "Register", "Continue as Guest"])
        
        if auth_option in ["Login", "Register"]:
            with st.form(f"{auth_option.lower()}_form"):
                username = st.text_input("Username")
                password = st.text_input("Password", type="password")
                
                if auth_option == "Register":
                    confirm_password = st.text_input("Confirm Password", type="password")
                    email = st.text_input("Email")
                
                submit = st.form_submit_button(auth_option)
                
                if submit:
                    if auth_option == "Login":
                        user_id = db.verify_user(username, password)
                        if user_id:
                            st.session_state.user_id = user_id
                            st.success("Login successful!")
                            st.rerun()
                        else:
                            st.error("Invalid username or password")
                    else:  # Register
                        if password != confirm_password:
                            st.error("Passwords do not match")
                        elif len(password) < 6:
                            st.error("Password must be at least 6 characters long")
                        else:
                            success, message = db.register_user(username, password, email)
                            if success:
                                st.success(message)
                                st.info("Please login with your new account")
                            else:
                                st.error(message)
    else:
        st.write(f"Logged in as: {st.session_state.user_id}")
        if st.button("Logout"):
            st.session_state.user_id = None
            st.rerun()

# Your existing app code here (the rest of your original app.py content)
# [Rest of your original app.py code goes here]
