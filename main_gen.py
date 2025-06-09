import streamlit as st
import langchain_helper as lch

st.set_page_config(page_title="Darija Chatbot", page_icon="💬")
st.title("Darija Chatbot")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# User input box
user_input = st.chat_input("Sawalek b Darija...")  # like ChatGPT's input

# When user submits a question
if user_input:
    response = lch.generate_content(user_input)
    st.session_state.chat_history.append(("user", user_input))
    st.session_state.chat_history.append(("assistant", response))

# Stylish chat history display
for role, message in st.session_state.chat_history:
    if role == "user":
        with st.chat_message("user"):
            st.markdown(f"🧑‍💬 **You**: {message}")
    else:
        with st.chat_message("assistant"):
            st.markdown(f"🤖 **Bot**: {message}")
