#!/bin/bash

# This script automates the deployment of the SymbioteSystems CEO Multi-Agent System
# on an Oracle Cloud Free Tier ARM VM (Ubuntu 22.04 Minimal).

# Exit immediately if a command exits with a non-zero status.
set -e

echo "Starting SymbioteSystems CEO Agent deployment..."

# 1. Update and install necessary packages
echo "Updating system packages and installing git, curl, docker, and docker-compose..."
sudo apt update
sudo apt install -y git curl docker.io docker-compose

# 2. Add current user to the docker group to run docker commands without sudo
echo "Adding current user to the docker group..."
sudo usermod -aG docker $USER

# Note: For the new group membership to take effect, the user needs to log out and log back in.
# For an automated script, we can activate it for the current session.
newgrp docker

echo "Docker and Docker Compose installed and configured."

# 3. Install Ollama (if not already installed via docker-compose)
echo "Installing Ollama..."
curl -fsSL https://ollama.com/install.sh | sh

# 4. Pull the desired Ollama model (e.g., llama3 or mistral)
# This assumes Ollama is running or will be started by docker-compose.
# We will pull it directly to ensure it's available for the Ollama container.
OLLAMA_MODEL=${OLLAMA_MODEL:-llama3}
echo "Pulling Ollama model: $OLLAMA_MODEL. This may take some time..."
ollama pull $OLLAMA_MODEL

# 5. Navigate to the project directory
echo "Navigating to project directory..."
cd /home/ubuntu/symbiote-ceo-agent

# 6. Copy .env.example to .env if it doesn't exist
if [ ! -f .env ]; then
  echo "Creating .env file from .env.example. Please edit it with your actual credentials."
  cp .env.example .env
else
  echo ".env file already exists. Skipping creation from .env.example."
fi

# 7. Start the Docker Compose services
echo "Starting Docker Compose services (Ollama, n8n, and SymbioteSystems Agent)..."
docker-compose up -d --build

echo "Deployment complete!"
echo "---------------------------------------------------"
echo "Ollama should be running on port 11434."
echo "n8n should be running on port 5678. Access it via http://<your_vm_public_ip>:5678"
echo "The SymbioteSystems CEO Agent system is running as a Docker container."
echo "
IMPORTANT: You need to configure n8n workflows and credentials manually."
echo "  - Import the JSON workflow files from the 'workflows' directory into n8n."
echo "  - Configure SMTP credentials for email sending."
echo "  - Configure social media API credentials for posting."
echo "  - Configure AI Image Generator credentials (e.g., Stability AI) and AWS S3 credentials for image generation/storage."
echo "  - Set up cron jobs in n8n to trigger the main.py script or specific agent tasks."
echo "
After n8n is configured, you can trigger the agent system by running 'python main.py' inside the symbiote-ceo-agent container,"
echo "or by setting up a webhook in n8n to trigger it."
