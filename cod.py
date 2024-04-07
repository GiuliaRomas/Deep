
def inicializacao():
    import os

    openai_api_key = os.getenv("OPENAI_API_KEY", "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")

    from langchain.document_loaders import TextLoader

    # Caminho da pasta no Google Drive onde estão os arquivos
    caminho_da_pasta = '/content/drive/MyDrive/deep/docs'

    # Lista para armazenar os documentos
    documents_list = []

    # Percorrer os diretórios e carregar os arquivos
    for root, dirs, files in os.walk(caminho_da_pasta):
        for nome_arquivo in files:
            if nome_arquivo.endswith('.txt'):  # Verificar se o arquivo é um arquivo de texto
                caminho_completo = os.path.join(root, nome_arquivo)
                print(f'caminho = {caminho_completo}')

                try:
                    loader = TextLoader(caminho_completo, autodetect_encoding=True)
                    documents = loader.load()
                    
                    # Adicionar o documento à lista de documentos
                    documents_list.extend(documents)
                except Exception as e:
                    print(f"Erro ao carregar o conteúdo do arquivo {nome_arquivo}: {e}")

    # Agora, documents_list contém todos os documentos carregados

    from langchain.text_splitter import CharacterTextSplitter

    #Chunks de 500 palavras
    text_splitter = CharacterTextSplitter(chunk_size=500)
    chunks = text_splitter.split_documents(documents_list)

    chunks[0:20]

    print(len(chunks))

    from langchain.embeddings import OpenAIEmbeddings
    from langchain.vectorstores import Weaviate
    import weaviate
    from weaviate.embedded import EmbeddedOptions

    client = weaviate.Client(
    embedded_options = EmbeddedOptions()
    )

    vectorstore = Weaviate.from_documents(
        client = client,
        documents = chunks,
        embedding = OpenAIEmbeddings(model="text-embedding-3-small", openai_api_key=openai_api_key),  #text-embedding-3-small usado para criar os embeddings
        by_text = False
    )

    retriever = vectorstore.as_retriever()

    from langchain.prompts import ChatPromptTemplate

    template = """Você é um assistente que irá responder retornando artigos e leis que podem ser aplicados no contexto fornecido.
    Sempre especifique o nome da lei ou do estatuto em que os artigos se encontram.
    Forneça explicação geral dos artigos e leis, considerando o contexto.
    Não invente.
    Use as seguintes peças de texto para responder a pergunta.
    Se não souber a resposta, apenas responda que não sabe a resposta.
    Use no máximo sete sentenças e mantenha a resposta concisa.
    Pergunta: {question}
    Contexto: {context}
    Resposta:/
    """
    prompt = ChatPromptTemplate.from_template(template)

    print(prompt)
    
    return openai_api_key, retriever, prompt

def gerar_resposta(openai_api_key, retriever, prompt, query):
    from langchain_openai import ChatOpenAI
    from langchain.schema.runnable import RunnablePassthrough
    from langchain.schema.output_parser import StrOutputParser

    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.0, openai_api_key=openai_api_key)

    rag_chain = (
        {"context": retriever,  "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    rag_chain.invoke(query)
    return rag_chain.get_output()
