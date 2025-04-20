# Concert Chatbot

A Streamlit-powered chatbot that answers questions about concerts using LangChain and SerpAPI, with Ollama model support.

![Streamlit App](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-00A67E?style=for-the-badge)
![ChromaDB](https://img.shields.io/badge/ChromaDB-FFD43B?style=for-the-badge)

## Features
- Real-time concert information via SerpAPI
- Natural language Q&A about events
- Docker support for easy deployment
- Ollama LLM integration

## Installation

### Local Development
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

## Running the App

To use the Streamlit app, you can run it locally.
1. Ensure your virtual environment is activated.
2. Install Streamlit:
   ```bash
   pip install streamlit
   ```
3. Run the application:
   ```bash
   streamlit run src/app.py
   ```

### Accessing the App
Once the app is running, you can access it at `http://localhost:8501` in your web browser.

## Usage

- Enter a question about concerts in the input box.
- Click "Ask" to get real-time answers.
- Use the "Ollama" toggle to switch between local LLM and SerpAPI responses.

## Contributing

Feel free to open issues or pull requests to improve this project!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Streamlit](https://streamlit.io/)
- [LangChain](https://langchain.readthedocs.io/)
- [SerpAPI](https://serpapi.com/)
- [Ollama](https://ollama.com/)

## How to Run Locally

Make sure you have Python 3.8+ installed and follow these steps:

1. Clone this repository:
   ```bash
   git clone https://github.com/tSopermon/ProvectusInternship_NikolaosTsopanidis.git
   cd ProvectusInternship_NikolaosTsopanidis
2. Set up the virtual environment and install dependencies as described in the "Installation" section.
3. Complete the "Ollama Setup" steps to install and run the required models.
4. Start the Streamlit application:
   ```bash
   streamlit run src/app.py
   ```
The app will be available at `http://localhost:8501`

## Configuration
Edit `.env` to customize:
   ```env
   SERPAPI_API_KEY=your_api_key
   ```