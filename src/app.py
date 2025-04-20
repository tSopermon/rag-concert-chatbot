"""
Code was inspired by the implementations described in the following sites
* https://medium.com/@mrcoffeeai/conversational-chatbot-trained-on-own-data-streamlit-and-langchain-a45ea5a9dc0f
* https://github.com/y-pred/Langchain/blob/main/Langchain%202.0/RAG_Conversational_Chatbot.ipynb
* https://python.langchain.com/v0.2/docs/tutorials/local_rag/
"""
import traceback
import streamlit as st
from utils.text_input import is_concert_related, get_vector_store
from utils.summary_generation import generate_summary
from utils.rag_chains import get_response
from utils.serpapi_function import get_events_for_artist
from langchain_core.messages import AIMessage
from config import SERPAPI_API_KEY, embeddings, summarizer, llm, CONCERT_RELATED_KEYWORDS, SUMMARY_INSTRUCTIONS

# ---------------------------------------------------------------------------------------------------------------
# initializing the vector store and chat history ----------------------------------------------------------------
chat_history=[]
vector_store=[]

# ---------------------------------------------------------------------------------------------------------------
# streamlit app -------------------------------------------------------------------------------------------------
style = "<style>h2 {text-align: center;}</style>"
st.markdown(style, unsafe_allow_html=True)
st.header("LangChain Concert chatbot")
st.write("<p style='text-align: center;'>This app is a concert chatbot that can answer questions about concerts.</p>", unsafe_allow_html=True)
# side Bar ------------------------------------------------------------------------------------------------------
st.sidebar.subheader("Upload Concert Document")
doc_text = st.sidebar.text_area("Paste your concert document here", height=200, key="doc_input")
if st.sidebar.button("Upload Document", key="doc_submit_button"):
    if not doc_text:
        st.warning("Please enter some text.")
    elif not is_concert_related(doc_text, CONCERT_RELATED_KEYWORDS):
        st.warning("Sorry, I cannot ingest documents with other themes.")
    else:
        with st.spinner("Processing document..."):
            try:
                summary = generate_summary(doc_text, SUMMARY_INSTRUCTIONS, summarizer, llm)
                if "chat_history" not in st.session_state:
                    st.session_state.chat_history = []
                if "vector_store" not in st.session_state:
                    st.session_state.vector_store = get_vector_store(doc_text, embeddings)  # Use full text for consistency
                    st.session_state.last_text = summary
                st.success("Your document has been successfully added to the database.")
                st.write(summary)
            except Exception as e:
                st.error(f"Error: {e}")
                print(traceback.format_exc())

# sidebar for artist event search (SerpApi Functionality)
st.sidebar.subheader("Search Artist Events")
artist_name = st.sidebar.text_input("Enter artist name (e.g., Lady Gaga)", key="artist_input")
if st.sidebar.button("Search Events", key="event_submit_button"):
    if not artist_name:
        st.warning("Please enter an artist name.")
    else:
        with st.spinner(f"Searching concerts for {artist_name}..."):
            try:
                events = get_events_for_artist(artist_name, SERPAPI_API_KEY)
                summary = generate_summary(events, SUMMARY_INSTRUCTIONS, summarizer, llm)
                if "chat_history" not in st.session_state:
                    st.session_state.chat_history = []
                if "vector_store" not in st.session_state:
                    st.session_state.vector_store = get_vector_store(events, embeddings)  # Use full events text
                    st.session_state.last_text = summary
                st.success(f"The upcoming events of {artist_name} have been successfully added to the database.")
                st.write(summary)
            except Exception as e:
                st.error(f"Error: {e}")
                print(traceback.format_exc())

# Chatbot interface ------------------------------------------------------------------------------------------------
user_input = st.text_input("Ask a quenstion:")
if st.button("Submit", key="question_submit_button"):
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

# custom theme
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