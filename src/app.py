import sys

import streamlit as st


if __name__ == "__main__":
    sys.path.append(".")

    st.set_page_config(
        page_title="Chat with the knowledge base",
        page_icon="💬",
        layout="centered",
        initial_sidebar_state="auto",
        menu_items=None,
    )

    st.title("How to start 📚")
    st.info("To start chatting with the knowledge base, please click the **chat** button in the sidebar.")
