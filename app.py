import streamlit as st
from chatbot import get_response

st.set_page_config(page_title="AI Chatbot", page_icon="🤖")
st.title("🤖 AI Chatbot")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# User input
user_input = st.text_input("You:", "")

if user_input:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Get bot response
    bot_response = get_response(user_input)
    st.session_state.messages.append({"role": "bot", "content": bot_response})

# Display chat history
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"**You:** {msg['content']}")
    else:
        st.markdown(f"**Bot:** {msg['content']}")
