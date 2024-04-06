# Set up the Streamlit app layout
st.title(" ChatGPT with Memory")
#st.subheader(" Powered by 🦜 LangChain + OpenAI + Streamlit")

hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)

# Let user select version
st.write("升级调试中，暂不可用")
st.write("GPT4.5 Turbo 上线了！无需注册就可以体验只有OpenAI付费用户才可以体验的GPT4.5了！")
version = st.selectbox("Choose ChatGPT version 请选择您想使用的ChatGPT版本", ("3.5", "4.5"))
if version == "3.5":
    # Use GPT-3.5 model
    MODEL = "gpt-3.5-turbo"
else:
    # USe GPT-4.5 model
    MODEL = "gpt-4"
    
# Ask the user to enter their OpenAI API key
#API_O = st.sidebar.text_input("API-KEY", type="password")
# Read API from Streamlit secrets
API_O = st.secrets["OPENAI_API_KEY"]
