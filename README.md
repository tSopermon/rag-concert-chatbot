# Concert Chatbot

A Streamlit-powered chatbot that answers questions about concerts using LangChain and SerpAPI, with Ollama model support.

![Streamlit App](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-00A67E?style=for-the-badge)
![ChromaDB](https://img.shields.io/badge/ChromaDB-FFD43B?style=for-the-badge)

## Features
- Natural language Q&A about events
- Ollama LLM integration
- Real-time concert information via SerpAPI

## Development Process of the App

The Concert Chatbot is a web app that answers questions about concerts using **Retrieval-Augmented Generation (RAG)**. Built with **LangChain**, **Ollama**, **Streamlit**, and **SerpAPI**, it processes concert documents and fetches real-time event data. For a detailed look at the code and explanations, see the Jupyter Notebook: [`notebooks/app_description.ipynb`](notebooks/app_description.ipynb).

1. **Setup**\
   Installed dependencies like **Streamlit** (web interface), **LangChain** (RAG pipelines), **langchain-ollama**/**langchain-chroma** (model and vector storage), and **SerpAPI** (event data).

2. **Model Configuration**\
   Used **Ollama** to set up:

   - **nomic-embed-text**: Creates vector embeddings for text.
   - **llama3.1:8b**: Generates summaries and responses with strict grounding.

3. **Document Processing**\

   - Validated concert documents with `is_concert_related` using keywords (e.g., "concert").
   - Summarized valid documents with the LLM and `ChatPromptTemplate`.
   - Split summaries into chunks (`RecursiveCharacterTextSplitter`) and stored vectors in **Chroma**.

4. **Event Retrieval**\
   Used **SerpAPI** (`get_events_for_artist`) to fetch and summarize up to three concert events, stored in Chroma.

5. **RAG Pipeline**\

   - Configured a **Chroma** retriever to fetch top 5 relevant chunks.
   - Used `create_history_aware_retriever` for context-aware retrieval.
   - Combined retrieval and LLM with `create_retrieval_chain` for conversational answers.

6. **Streamlit Interface**\

   - **Sidebar**: Upload documents or search events.
   - **Chat Interface**: Ask questions, view responses, and conversation history (`st.session_state`).
   - Added error handling for empty inputs.

7. **Testing**
   Ensured document validation, event retrieval, and RAG accuracy. Inspired by LangChain docs and Medium articles.

The result is a robust chatbot for concert enthusiasts. Explore details in [`notebooks/app_description.ipynb`](notebooks/app_description.ipynb).

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/tSopermon/ProvectusInternship_NikolaosTsopanidis.git
   cd ProvectusInternship_NikolaosTsopanidis
   ```
2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate    # Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Configure environment variables:
   ```bash
   echo "SERPAPI_API_KEY=your_key_here" > .env
   ```

### Ollama Setup
**Important**: The Concert Chatbot relies on Ollama models for its core functionality. Specifically, it requires nomic-embed-text for embeddings and llama3.1:8b for answering and summarizing. Without these models, the app will not function as intended. Follow the steps below to install and set up Ollama:
1. Install Ollama:
 * Download and install Ollama from the official Ollama [download page](https://ollama.com/download). Follow the instructions specific to your operating system.
2. Pull the required models:
 * Open a terminal and run the following commands to download the necessary models:
   ```bash
   ollama pull nomic-embed-text
   ollama pull llama3.1:8b
   ```
3. Start the Ollama server:
 * Ensure the Ollama server is running by executing:
   ```bash
   ollama serve
   ```

### Running the App
1. Ensure your virtual environment is activated.
2. Run the application:
   ```bash
   streamlit run src/app.py
   ```
3. Once the app is running, you can access it at `http://localhost:8501` in your web browser.

## How to Use the App

1. **Upload a Concert Document**  
   - Use the sidebar's text box to enter a concert-related document.  
   - Press the "Upload" button to update the database and generate a summary of the document.

2. **Ask Questions**  
   - Once the document is uploaded, type your question about the document in the main input box.  
   - The app will provide accurate answers based on the uploaded content.

3. **Explore Concert Information**  
   - Search for upcoming concerts or events by entering an artist's name.  
   - Get real-time details like dates and locations using SerpAPI integration.

## Contributing

Feel free to open issues or pull requests to improve this project!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

* [Amina Javaid](https://medium.com/@aminajavaid30/building-a-rag-system-the-data-ingestion-pipeline-d04235fd17ea)
* [Akshat Rai Laddha](https://medium.com/@laddhaakshatrai/how-to-perform-data-ingestion-with-langchain-day-12-100-f11288d7ae99)
* [Ariffud Muhammad](https://www.hostinger.com/tutorials/what-is-ollama#Key_features_of_Ollama)
* [DhanushKumar](https://medium.com/@danushidk507/rag-with-llama-using-ollama-a-deep-dive-into-retrieval-augmented-generation-c58b9a1cfcd3)
* [An Jiang](https://medium.com/@jiangan0808/retrieval-augmented-generation-rag-with-open-source-hugging-face-llms-using-langchain-bd618371be9d)
* [LangChain.com RAG App tutorial](https://python.langchain.com/docs/tutorials/rag/)
* [LangChain.com Local RAG tutorial](https://python.langchain.com/v0.2/docs/tutorials/local_rag/)
* [Ashish Malhotra](https://medium.com/@mrcoffeeai/conversational-chatbot-trained-on-own-data-streamlit-and-langchain-a45ea5a9dc0f)
* [Ashish Malhotra/y-pred](https://github.com/y-pred/Langchain/blob/main/Langchain%202.0/RAG_Conversational_Chatbot.ipynb)