import streamlit as st
from langchain_community.llms import Ollama
import cod as cod

st.markdown("<h1 style='font-size:38px;'>⚖️ Pesquisa por Fundamento Jurídico</h1>", unsafe_allow_html=True)
# escrever no sidebar
st.sidebar.markdown('## 📄 Sobre a aplicação:')
# escrever no sidebar com letras menores
st.sidebar.caption('É uma ferramenta que tem o intuito de facilitar a busca por artigos e leis para fundamentar peças jurídicas')

# colocar divisoria no sidebar
st.sidebar.markdown('---')

openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')

openai_api_key, retriever, prompt = cod.inicializacao()

def generate_response(query, openai_api_key=openai_api_key, retriever=retriever, prompt=prompt):
    output = cod.gerar_resposta(openai_api_key, retriever, prompt, query)
    st.write(output)    
    
with st.form('my_form'):
    text = st.text_area('Digite o contexto:', 'Para qual contexto você precisa de fundamento jurídico?')
    
    submitted = st.form_submit_button('Enviar')
    
    if not openai_api_key.startswith('sk-'):
        st.warning('Por favor, entre com sua OpenAi API key!', icon='⚠')
    if submitted and openai_api_key.startswith('sk-'):
        generate_response(text)