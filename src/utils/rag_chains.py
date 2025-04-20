from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain.chains import create_retrieval_chain, create_history_aware_retriever
from langchain.chains.combine_documents import create_stuff_documents_chain
import streamlit as st

def get_retriever_chain(vector_store, llm):
    """
    Return the retriever chain for the vector store.
    args:
        vector_store: Chroma vector store.
        llm: language model to be used.
    returns:
        history_retriever_chain: retriever chain for the vector store.
    """
    retriever = vector_store.as_retriever(search_kwargs={"k": 5})   # retrieve 5 most similar documents
    prompt = ChatPromptTemplate.from_messages([MessagesPlaceholder(variable_name="chat_history"), 
                                               ("user","{input}"), 
                                               ("user","Given the following conversation, answer the question")])
    history_retriever_chain = create_history_aware_retriever(llm, retriever, prompt)

    return history_retriever_chain

def get_conversational_rag(history_retriever_chain, llm):
    """
    Return the conversational RAG chain.
    args:
        history_retriever_chain: retriever chain for the vector store.
        llm: language model to be used.
    returns:
        conversational_retrieval_chain: conversational RAG chain.
    """
    answer_prompt = ChatPromptTemplate.from_messages([("system","Answer the question based on the context below: \n\n{context}"), 
                                                      MessagesPlaceholder(variable_name="chat_history"), 
                                                      ("user","{input}")])
    document_chain = create_stuff_documents_chain(llm, answer_prompt)
    conversational_retrieval_chain = create_retrieval_chain(history_retriever_chain, document_chain)

    return conversational_retrieval_chain

def get_response(user_input, llm):
    """
    Return the response from the chatbot.
    args:
        user_input (str): user input to be processed.
        llm: language model to be used.
    returns:
        response (str): response from the chatbot.
    """
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