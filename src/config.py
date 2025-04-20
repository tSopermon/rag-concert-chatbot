"""
Here we store model configurations, variables, and constants for the app
"""
from langchain_ollama import OllamaEmbeddings, ChatOllama
from transformers import pipeline
from dotenv import load_dotenv
import os

load_dotenv() # to load SerpApi key from .env file
SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY")

embeddings = OllamaEmbeddings(model="nomic-embed-text")
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
llm = ChatOllama(model="llama3.1:8b", grounding="strict")

CONCERT_RELATED_KEYWORDS = ["concert", "music", "band", "performance", "stage", 
                            "ticket", "venue", "artist", "festival", "tour", "gig", 
                            "show", "orchestra", "symphony", "recital", "live music", 
                            "audience", "encore", "setlist", "soundcheck"]

SUMMARY_INSTRUCTIONS = """
    You are a concert summarizer. Your task is to summarize the concert document based on the given instructions.
    You should focus on the main points, key events, and any important details that are relevant to the concert.
    The summary should be concise and informative, providing a clear overview of the concert document.
    You should not include any personal opinions or subjective interpretations.
    Your summary should be in a clear and easy-to-understand format, using simple language and avoiding jargon.
    If the document appears to be in JSON format, you should extract the relevant information and summarize it accordingly
    and not mention the JSON format in the summary.
    """