import streamlit as st
from langserve import RemoteRunnable


@st.cache_resource(show_spinner=False)
def get_conversation_agent_chain(chat_engine_url: str):
    return RemoteRunnable(chat_engine_url)
