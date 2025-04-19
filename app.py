# https://medium.com/@mrcoffeeai/conversational-chatbot-trained-on-own-data-streamlit-and-langchain-a45ea5a9dc0f
# https://github.com/y-pred/Langchain/blob/main/Langchain%202.0/RAG_Conversational_Chatbot.ipynb
# https://python.langchain.com/v0.2/docs/tutorials/local_rag/
import os, re
import traceback
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaEmbeddings
from langchain_ollama import ChatOllama
from langchain_chroma import Chroma
from transformers import pipeline
from langchain_core.documents import Document
from langchain_text_splitters import CharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.messages import AIMessage
from langchain.chains import create_retrieval_chain, create_history_aware_retriever
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder

# return chroma vector store for the text
def get_vector_store(text, embeddings):
    processed_text = re.sub(r'\s+', ' ', text)
    processed_text = re.sub(r'[^a-zA-Z0-9\s]', '', processed_text)
    documents = [Document(page_content=processed_text)]
    text_splitter = CharacterTextSplitter(
        separator="\n\n",
        chunk_size=300,
        chunk_overlap=100,
        length_function=len
        )
    chunks = text_splitter.split_documents(documents)
    chunk_texts = [chunk.page_content for chunk in chunks]
    vector_store = Chroma.from_texts(
        texts=chunk_texts,
        embedding=embeddings,
        persist_directory="chroma_db",  # directory to persist the database
        collection_name="my_collection"  # name of the collection
        )
    return vector_store

def get_retriever_chain(vector_store, llm):
    retriever = vector_store.as_retriever(search_kwargs={"k": 5}) # retrieve 5 most similar documents
    prompt = ChatPromptTemplate.from_messages([
        MessagesPlaceholder(variable_name="chat_history"),
        ("user","{input}"),
        ("user","Given the following conversation, summarize the documents and answer the question")
    ])
    history_retriever_chain = create_history_aware_retriever(llm, retriever, prompt)
    return history_retriever_chain

def get_conversational_rag(history_retriever_chain, llm):
    answer_prompt = ChatPromptTemplate.from_messages([
        ("system","Answer the question based on the context below: \n\n{context}"),
        MessagesPlaceholder(variable_name="chat_history"),
        ("user","{input}")
    ])
    document_chain = create_stuff_documents_chain(llm, answer_prompt)
    conversational_retrieval_chain = create_retrieval_chain(history_retriever_chain, document_chain)

    return conversational_retrieval_chain

def get_response(user_input, llm):
  formatted_chat_history = [
        message.content if hasattr(message, 'content') else str(message)
        for message in st.session_state.chat_history
    ]
  
  history_retriever_chain = get_retriever_chain(st.session_state.vector_store, llm)
  conversation_rag_chain = get_conversational_rag(history_retriever_chain, llm)
  response = conversation_rag_chain.invoke({
        "chat_history":formatted_chat_history,
        "input":user_input
    })
  return response["answer"]

# configuring embeddings and model
embeddings = OllamaEmbeddings(model="nomic-embed-text")

# configuring summarization model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# configuring the HuggingFace conversational pipeline
llm = ChatOllama(model="llama3.1:8b",)

chat_history=[]
vector_store=[]

# streamlit app --------------------------------------------------------
st.header('LangChain Doc Summary')
st.write("This app summarizes documents using LangChain and Chroma.")
chat_history=[]

st.markdown(
    """
    <style>
    [data-testid="stSidebar"] {
        width: 300px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Text input
st.sidebar.subheader("Upload Document")
with st.sidebar:
    text = st.text_area("Enter text", height=200, help="Paste your concert document to update the database.")
    if st.button("Submit text"):
        if not text:
            st.warning("Please enter some text.")
        else:
            # generate the text's summary
            with st.spinner("Processing..."):
                try:
                    summary = summarizer(text, max_length=200, min_length=30, do_sample=False)
                    st.success("Summary: ")
                    st.write(summary[0]['summary_text'])
                    if "chat_history" not in st.session_state:
                        st.session_state.chat_history=[]
                    if vector_store not in st.session_state:
                        st.session_state.vector_store = get_vector_store(text, embeddings)
                        st.session_state.last_text = text
                    st.success("Text successfully added to the database.")
                except Exception as e:
                    st.error(f"Error: {e}")
                    print(traceback.format_exc())

# Chatbot interface -------------------------------------------------
st.subheader("Chatbot")
st.write("Ask questions about the documents in the database.")
user_input = st.text_input("Ask a quenstion:")
# press enster or submit button
if st.button("Submit"):
    if not user_input:
        st.warning("Please enter a question.")
    else:
        with st.spinner("Generating response..."):
            try:
                if user_input is None and user_input == "":
                    st.warning("Please enter a question.")
                else:
                    response = get_response(user_input, llm)
                    st.session_state.chat_history.append(AIMessage(content=response))

                for message in st.session_state.chat_history:
                    if isinstance(message, AIMessage):
                        with st.chat_message("AI"):
                            st.write(message.content)
            except Exception as e:
                st.error(f"Error: {e}")
                print(traceback.format_exc())