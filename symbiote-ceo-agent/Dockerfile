FROM python:3.11-slim-buster

WORKDIR /app

# Install system dependencies for Ollama (if any specific ones are needed for its client)
# and other potential tools. For now, assuming basic Python environment is enough.
RUN apt-get update && apt-get install -y \
    git \
    curl \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expose a port if you plan to add a web dashboard later
# EXPOSE 8000

CMD ["python", "main.py"]
