# Concert Chatbot

A Streamlit-powered chatbot that answers questions about concerts using LangChain and SerpAPI, with optional Ollama model support.

![Streamlit App](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-00A67E?style=for-the-badge)
![ChromaDB](https://img.shields.io/badge/ChromaDB-FFD43B?style=for-the-badge)

## Features
- Real-time concert information via SerpAPI
- Natural language Q&A about events
- Docker support for easy deployment
- Optional Ollama LLM integration

## Installation

### Local Development
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/concert-chatbot.git
   cd concert-chatbot
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
### Docker Setup
1. Build the image:
   ```bash
   docker build -t concert-chatbot .
   ```
2. Run the container:
   ```bash
   docker run -p 8501:8501 -e SERPAPI_API_KEY=your_key_here concert-chatbot
   ```
## Running the App

To run the Streamlit app, you can either use Docker or run it locally.

### Local
1. Ensure your virtual environment is activated.
2. Install Streamlit:
   ```bash
   pip install streamlit
   ```
3. Run the application:
   ```bash
   streamlit run src/app.py
   ```

### Docker
If you're using Docker, follow these steps:

1. Build the Docker image:
   ```bash
   docker build -t concert-chatbot .
   ```
2. Run the Docker container:
   ```bash
   docker run -p 8501:8501 -e SERPAPI_API_KEY=your_key_here concert-chatbot
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
```

## How to Run Locally

Make sure you have Python 3.8+ installed and follow these steps:

1. Clone this repository:
   ```bash
   git clone
Start the Streamlit application:
   ```bash
   streamlit run src/app.py
   ```

The app will be available at `http://localhost:8501`

## Ollama Setup
For local LLM functionality:
1. Install [Ollama](https://ollama.com/download)
2. Pull required models:
   ```bash
   ollama pull nomic-embed-text
   ollama pull llama3:8b
   ```
3. Ensure Ollama server is running

## Configuration
Edit `.env` to customize:
   ```env
   SERPAPI_API_KEY=your_api_key
   ```