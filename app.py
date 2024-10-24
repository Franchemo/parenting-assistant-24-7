import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

# Page configuration must be the first Streamlit command
st.set_page_config(page_title="AI Parenting Assistant | AI育儿助手", page_icon="👶", layout="wide")

# Load environment variables
load_dotenv()

# Set up OpenAI API key and Assistant ID
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ASSISTANT_ID = os.getenv("OPENAI_ASSISTANT_ID")

# Initialize OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)

# Custom CSS
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

# Language selection
if "language" not in st.session_state:
    st.session_state.language = "en"

# Language dictionary
LANG = {
    "en": {
        "title": "AI Parenting Assistant",
        "subtitle": "Get real-time parenting advice to enhance your parenting decisions",
        "child_age": "Child's Age",
        "child_personality": "Child's Personality Traits",
        "kindergarten": "Is your child in kindergarten?",
        "interests": "Child's Interests and Hobbies",
        "languages": "Languages spoken at home (including dialects)",
        "family_members": "Number of family members living with the child",
        "siblings": "Does your child have siblings?",
        "siblings_age": "Siblings' ages",
        "start_chat": "Start Chat",
        "question_type": "Select Question Type",
        "question_types": ["Parenting Issues", "Health Concerns", "Behavior Management"],
        "subcategories": ["Sleep", "Diet", "Early Education", "Other"],
        "input_placeholder": "Enter your parenting question to get real-time advice",
        "clear_chat": "Clear Chat",
        "thinking": "AI Assistant is thinking...",
        "user_info_title": "To provide more personalized solutions, please answer the following questions:",
        "yes": "Yes",
        "no": "No",
        "view_info": "View User Information",
        "submit": "Submit"
    },
    "zh": {
        "title": "AI育儿助手",
        "subtitle": "获取实时育儿建议，提升您的育儿决策效率",
        "child_age": "您孩子的年龄",
        "child_personality": "您孩子的性格特征",
        "kindergarten": "您孩子是否在上幼儿园",
        "interests": "您孩子平时有什么兴趣爱好",
        "languages": "您在家说几种语言（包括方言）",
        "family_members": "您家常和孩子住在一起的有几个人",
        "siblings": "您家孩子是否有兄弟姐妹",
        "siblings_age": "兄弟姐妹多大",
        "start_chat": "开始对话",
        "question_type": "选择问题类型",
        "question_types": ["育儿问题", "健康问题", "行为管理"],
        "subcategories": ["睡眠", "饮食", "早教", "其他"],
        "input_placeholder": "输入您的育儿问题，获得实时建议",
        "clear_chat": "清空对话",
        "thinking": "AI助手正在思考中...",
        "user_info_title": "为了能够提供更加个性化的解决方案，请您回答以下几个问题：",
        "yes": "是",
        "no": "否",
        "view_info": "查看用户信息",
        "submit": "提交"
    }
}

# Language selector in the sidebar
st.sidebar.selectbox(
    "Language | 语言",
    ["English", "中文"],
    key="lang_select",
    on_change=lambda: setattr(st.session_state, "language", "en" if st.session_state.lang_select == "English" else "zh")
)

# Get current language
lang = LANG[st.session_state.language]

# Update the Assistant instructions based on language
try:
    assistant = client.beta.assistants.update(
        assistant_id=ASSISTANT_ID,
        model="gpt-4-turbo-preview",
        instructions=f"""You are an AI parenting assistant. Provide concise, practical, and personalized advice for parents.
        Respond in {st.session_state.language_select}.
        Consider the context of previous messages in the conversation to tailor your responses.
        Use the information provided about the child's age, personality, family situation, and other details to give highly targeted advice.
        Be empathetic and supportive in your responses."""
    )
except Exception as e:
    st.error(f"Error updating assistant: {str(e)}")
    st.stop()

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "thread_id" not in st.session_state:
    st.session_state.thread_id = client.beta.threads.create().id
if "user_info" not in st.session_state:
    st.session_state.user_info = {}
if "show_chat" not in st.session_state:
    st.session_state.show_chat = False

def generate_ai_response(prompt):
    try:
        client.beta.threads.messages.create(
            thread_id=st.session_state.thread_id,
            role="user",
            content=prompt
        )

        run = client.beta.threads.runs.create(
            thread_id=st.session_state.thread_id,
            assistant_id=ASSISTANT_ID
        )

        with st.spinner(lang["thinking"]):
            while run.status not in ["completed", "failed"]:
                run = client.beta.threads.runs.retrieve(
                    thread_id=st.session_state.thread_id,
                    run_id=run.id
                )
                if run.status == "failed":
                    return "Sorry, the AI assistant couldn't generate a response. Please try again." if st.session_state.language == "en" else "抱歉，AI助手无法生成回答。请稍后再试。"

        messages = client.beta.threads.messages.list(thread_id=st.session_state.thread_id)
        return messages.data[0].content[0].text.value

    except Exception as e:
        return f"Error generating response: {str(e)}" if st.session_state.language == "en" else f"生成回答时出现了错误: {str(e)}"

# Main title
col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.title(f"🤖 {lang['title']}")
    st.subheader(lang["subtitle"])

# User information collection form
if not st.session_state.show_chat:
    st.markdown(f"### {lang['user_info_title']}")
    
    with st.form("user_info_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            st.session_state.user_info["child_age"] = st.text_input(lang["child_age"])
            st.session_state.user_info["child_personality"] = st.text_area(lang["child_personality"])
            st.session_state.user_info["kindergarten"] = st.selectbox(
                lang["kindergarten"],
                [lang["yes"], lang["no"]]
            )
            st.session_state.user_info["interests"] = st.text_area(lang["interests"])
        
        with col2:
            st.session_state.user_info["languages"] = st.text_input(lang["languages"])
            st.session_state.user_info["family_members"] = st.number_input(
                lang["family_members"],
                min_value=1,
                value=1
            )
            has_siblings = st.selectbox(
                lang["siblings"],
                [lang["yes"], lang["no"]]
            )
            if has_siblings == lang["yes"]:
                st.session_state.user_info["siblings_age"] = st.text_input(lang["siblings_age"])
        
        submit = st.form_submit_button(lang["start_chat"])
        if submit and st.session_state.user_info["child_age"]:
            st.session_state.show_chat = True
            st.rerun()

# Chat interface
if st.session_state.show_chat:
    # Display user info summary
    with st.expander(lang["view_info"], expanded=False):
        for key, value in st.session_state.user_info.items():
            st.write(f"{lang[key]}: {value}")
    
    # Question type selection
    question_type = st.selectbox(
        lang["question_type"],
        lang["question_types"],
        key="question_type"
    )

    # Conditional input for parenting subcategory
    parenting_subcategory = None
    if question_type == lang["question_types"][0]:  # Parenting Issues
        parenting_subcategory = st.selectbox(
            "📚 " + (lang["question_type"] if st.session_state.language == "zh" else "Select Specific Topic"),
            lang["subcategories"],
            key="parenting_subcategory"
        )

    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # User input
    user_input = st.chat_input(lang["input_placeholder"])

    if user_input:
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": user_input})
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(user_input)
        
        # Generate AI response
        prompt = f"""
User Information:
Child's Age: {st.session_state.user_info['child_age']}
Personality Traits: {st.session_state.user_info['child_personality']}
In Kindergarten: {st.session_state.user_info['kindergarten']}
Interests: {st.session_state.user_info['interests']}
Languages at Home: {st.session_state.user_info['languages']}
Family Members: {st.session_state.user_info['family_members']}
{f"Siblings' Ages: {st.session_state.user_info['siblings_age']}" if 'siblings_age' in st.session_state.user_info else ""}

Question Type: {question_type}
{f"Specific Topic: {parenting_subcategory}" if parenting_subcategory else ""}
Question: {user_input}

Please provide personalized parenting advice based on the user information and conversation history.
Respond in {'English' if st.session_state.language == 'en' else '中文'}.
        """
        
        ai_response = generate_ai_response(prompt)
        
        # Add AI response to chat history
        st.session_state.messages.append({"role": "assistant", "content": ai_response})
        
        # Display AI response
        with st.chat_message("assistant"):
            st.markdown(ai_response)

    # Clear chat button
    if st.button(lang["clear_chat"]):
        st.session_state.messages = []
        st.session_state.thread_id = client.beta.threads.create().id
        st.rerun()
