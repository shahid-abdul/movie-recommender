# Use official Python image
FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Install required packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app
COPY . .

# Expose port
EXPOSE 8080

# Run streamlit
CMD ["streamlit", "run", "app.py", "--server.port=8080", "--server.enableCORS=false"]
