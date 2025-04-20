FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# source code and .env
COPY src/ ./src/
COPY .env .env

# directory for Chroma persistence
RUN mkdir -p chroma_db

# Streamlit port
EXPOSE 8501

# binds 0.0.0.0 to allow external access for ollama server and streamlit
CMD ["streamlit", "run", "src/app.py", "--server.port=8501", "--server.address=0.0.0.0"]