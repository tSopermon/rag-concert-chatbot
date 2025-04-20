import re
from langchain_core.documents import Document
from langchain_text_splitters import CharacterTextSplitter
from langchain_chroma import Chroma

def is_concert_related(text, CONCERT_RELATED_KEYWORDS):
    """
    Check if the text contains any concert-related keywords.
    """
    text_lower = text.lower()
    return any(keyword in text_lower for keyword in CONCERT_RELATED_KEYWORDS)

def get_vector_store(text, embeddings):
    """
    Return Chroma vector store for the text.
    args:
        text (str): text to be processed.
        embeddings: embeddings model to be used.
    returns:
        vector_store: chroma vector store.
    """
    processed_text = re.sub(r'\s+', ' ', text)
    processed_text = re.sub(r'[^a-zA-Z0-9\s]', '', processed_text)
    documents = [Document(page_content=processed_text)]
    text_splitter = CharacterTextSplitter(separator="\n\n",
                                          chunk_size=300,
                                          chunk_overlap=100,
                                          length_function=len)
    chunks = text_splitter.split_documents(documents)
    chunk_texts = [chunk.page_content for chunk in chunks]
    vector_store = Chroma.from_texts(texts=chunk_texts,
                                     embedding=embeddings,
                                     persist_directory="chroma_db",     # directory to persist the database
                                     collection_name="my_collection")   # name of the collection
    
    return vector_store