FROM python:3.11-slim-buster

WORKDIR /app
COPY . /app

# Install system packages
RUN apt update -y && apt install -y awscli ffmpeg libsm6 libxext6 unzip

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Create Streamlit config for port 8080
RUN mkdir -p /root/.streamlit
RUN echo "\
    [server]\n\
    port = 8080\n\
    enableCORS = false\n\
    headless = true\n\
    \n\
    " > /root/.streamlit/config.toml

# Expose port
EXPOSE 8080

# Run Streamlit app
CMD ["streamlit", "run", "app.py"]
