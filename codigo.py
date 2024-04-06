from openai import OpenAI
import streamlit as st

st.title("Pequisa por embasamento legal")
st.set_page_config(page_title="Pequisa por embasamento legal", page_icon=":book:", layout="wide")

st.caption("🚀 A streamlit chatbot powered by OpenAI LLM")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])
