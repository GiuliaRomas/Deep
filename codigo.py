import streamlit as st
#st.title("Pequisa por embasamento legal")
st.set_page_config(page_title="Pequisa por embasamento legal", page_icon=":book:", layout="wide")

if "messages" not in st.session_state:
  st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

  
