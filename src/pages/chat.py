import uuid

import streamlit as st

from src.helper.app_utils import get_conversation_agent_chain
from src.helper.constants import CHAT_ENGINE_URL


st.set_page_config(
    page_title="Chat with the knowledge base",
    page_icon="💬",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items=None,
)
st.title("Chat with the knowledge base 💬")

start_new_chat = st.sidebar.button("Start New Chat", type="primary")

# Initialize the chat messages history
if "messages" not in st.session_state.keys() or start_new_chat:
    st.session_state.session_id = str(uuid.uuid4())
    st.session_state.messages = [{"role": "assistant", "content": "Я готовий відповісти на твої питання!"}]

st.sidebar.info(f"Session ID: {st.session_state.session_id}", icon="ℹ️")

# Initialize the chat engine
if "chat_engine" not in st.session_state.keys():
    st.session_state.chat_engine = get_conversation_agent_chain(CHAT_ENGINE_URL)

# Prompt for user input and save to chat history
if prompt := st.chat_input("Your question"):
    st.session_state.messages.append({"role": "user", "content": prompt})

# Display the prior chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# If last message is not from assistant, generate a new response
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = st.session_state.chat_engine.invoke(
                {
                    "question": prompt,
                    "session_id": st.session_state.session_id,
                }
            )
            response = response["agent_outcome"]["answer"]
            st.write(response)
            message = {"role": "assistant", "content": response}
            st.session_state.messages.append(message)
