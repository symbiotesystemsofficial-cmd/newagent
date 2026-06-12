# SymbioteSystems Autonomous CEO Multi-Agent System

This project implements a 24/7 autonomous CEO multi-agent system for "SymbioteSystems" using CrewAI, Ollama, and n8n. The system is designed to handle various business operations autonomously, from content strategy and social media management to sales and marketing.

## Table of Contents
1.  [Introduction](#introduction)
2.  [Features](#features)
3.  [Architecture](#architecture)
4.  [Prerequisites](#prerequisites)
5.  [Setup Guide](#setup-guide)
    -   [Oracle Cloud Free Tier Setup](#oracle-cloud-free-tier-setup)
    -   [Ollama Installation](#ollama-installation)
    -   [n8n Installation](#n8n-installation)
    -   [Agent System Setup](#agent-system-setup)
6.  [Running the System](#running-the-system)
    -   [Manual Execution via CLI](#manual-execution-via-cli)
    -   [Automated Scheduling with n8n](#automated-scheduling-with-n8n)
7.  [Customization](#customization)
8.  [Troubleshooting](#troubleshooting)
9.  [Contributing](#contributing)
10. [License](#license)

## 1. Introduction

SymbioteSystems is a business focused on AI, automation, digital products, and cybersecurity. This autonomous multi-agent system aims to manage and grow the business operations for products like "The AI Fraud Survival Manual" and "The Ultimate Agency OS" across various social media channels (TikTok, Instagram, Facebook, X, Threads, Pinterest, YouTube).

## 2. Features

-   **Autonomous Operation:** Runs 24/7 without manual intervention.
-   **Cost-Effective:** Utilizes Oracle Cloud Free Tier, Ollama with local LLMs, and self-hosted n8n for zero ongoing costs.
-   **Multi-Agent Architecture:** Comprises a CEO agent orchestrating specialized sub-agents for content, research, social media, sales, marketing, and design.
-   **CrewAI Framework:** Leverages CrewAI for robust agent orchestration.
-   **Local LLM Integration:** Uses Ollama with Llama 3 or Mistral for AI capabilities.
-   **External Integrations:** n8n for seamless integration with social media platforms, email services, and other APIs.
-   **Persistence:** ChromaDB for memory and context persistence.
-   **Deployment:** One-command deployment script for Oracle Cloud Free Tier.
-   **CLI Interface:** Simple command-line interface for manual goal input and status checks.

## 3. Architecture

The system is built around a hierarchical multi-agent architecture:

-   **CEO Agent (Orchestrator):** Receives high-level goals, breaks them into tasks, delegates to sub-agents, monitors completion and quality, and sends daily reports.
-   **Content Strategist Agent:** Plans weekly content calendar, generates post ideas, writes captions, scripts, hooks, and maintains brand voice consistency.
-   **Research Agent:** Monitors AI/automation/cybersecurity trends, tracks competitor activity, finds viral content patterns, and compiles trend reports.
-   **Social Media Manager Agent:** Schedules and publishes posts, monitors engagement, responds to comments/DMs, and tracks analytics.
-   **Sales & Marketing Agent:** Manages product promotion cycles, writes email sequences, optimizes CTAs and funnels, and tracks conversion metrics.
-   **Design Agent:** Generates carousel images, creates social media graphics, and maintains brand consistency.

## 4. Prerequisites

Before you begin, ensure you have the following:

-   An Oracle Cloud Infrastructure (OCI) account (Free Tier eligible).
-   Basic understanding of Linux command line.
-   A local machine with SSH access to your OCI VM.

## 5. Setup Guide

### Oracle Cloud Free Tier Setup

1.  **Sign up for Oracle Cloud Free Tier:** If you don't have an account, sign up [here](https://www.oracle.com/cloud/free/).
2.  **Create an Always Free ARM VM Instance:**
    -   Navigate to `Compute` -> `Instances`.
    -   Click `Create Instance`.
    -   Choose an `Always Free` eligible shape (e.g., `VM.Standard.A1.Flex` with 4 OCPUs and 24 GB RAM).
    -   Select an Ubuntu operating system image (e.g., `Ubuntu 22.04 Minimal`).
    -   Configure networking, ensuring public IP assignment. Make sure to open ports `11434` (for Ollama) and `5678` (for n8n) in your VCN's security list.
    -   Add your SSH public key for secure access.
    -   Click `Create`.
3.  **Connect to your VM:** Once the instance is running, use SSH to connect:
    ```bash
    ssh -i /path/to/your/private_key ubuntu@<your_vm_public_ip>
    ```

### Deployment Script

Once connected to your Oracle Cloud VM, you can use the provided `deploy.sh` script to set up Docker, Docker Compose, Ollama, and the agent system.

1.  **Clone the repository to your VM:**
    ```bash
    git clone <repository_url> /home/ubuntu/symbiote-ceo-agent
    cd /home/ubuntu/symbiote-ceo-agent
    ```
    *(Note: Replace `<repository_url>` with the actual URL if this project were hosted on GitHub, for example. For this exercise, assume the files are already in `/home/ubuntu/symbiote-ceo-agent`)*

2.  **Run the deployment script:**
    ```bash
    chmod +x deploy.sh
    ./deploy.sh
    ```
    This script will:
    -   Update system packages.
    -   Install Docker and Docker Compose.
    -   Add your user to the `docker` group.
    -   Install Ollama and pull the `llama3` model (or `mistral` if `OLLAMA_MODEL` is set in `.env`).
    -   Copy `.env.example` to `.env` if it doesn't exist.
    -   Build and start the Docker containers for Ollama, n8n, and the SymbioteSystems agent.

### n8n Configuration

n8n is crucial for external integrations and scheduling. After running `deploy.sh`, n8n will be accessible via your VM's public IP.

1.  **Access n8n:** Open your web browser and navigate to `http://<your_vm_public_ip>:5678`.
    -   You will be prompted to set up an admin user. Complete this step.
    -   If basic authentication is enabled (as in `docker-compose.yml`), use the `N8N_USERNAME` and `N8N_PASSWORD` defined in your `.env` file.

2.  **Import Workflows:**
    -   In the n8n UI, click on `Workflows` in the left sidebar.
    -   Click `New` -> `Import from JSON`.
    -   Import each `.json` file from the `/workflows/` directory (`send-email.json`, `post-social-media.json`, `generate-image.json`, `web-scrape.json`).

3.  **Configure Credentials:** For each imported workflow, you will need to set up credentials for the external services it interacts with.
    -   **Email (SMTP):** For `send-email.json`, configure an SMTP credential (e.g., Gmail, SendGrid, Mailgun). You'll need to provide host, port, username, and password.
    -   **Social Media:** For `post-social-media.json`, you'll need to set up credentials for each social media platform (Facebook, Instagram, X, etc.). This typically involves OAuth2 authentication or API keys/tokens. The example workflow uses a generic HTTP Request node, which will need to be adapted to specific social media APIs (e.g., Facebook Graph API, Twitter API v2). You might need to add specific nodes for each platform (e.g., 'Facebook' node, 'Twitter' node) and configure their respective credentials.
    -   **AI Image Generator:** For `generate-image.json`, configure credentials for your chosen AI image generation service (e.g., Stability AI, OpenAI DALL-E, Midjourney API). This will typically be an API key.
    -   **AWS S3 (or compatible storage):** For `generate-image.json` (if you want to store generated images), configure AWS S3 credentials (Access Key ID, Secret Access Key, Region). You can also use other S3-compatible storage services.

    *Detailed instructions for setting up each credential type can be found in the n8n documentation.* 

4.  **Activate Workflows:** After importing and configuring credentials, make sure to activate each workflow by toggling the `Active` switch in the n8n UI.

### Agent System Setup

1.  **Configure `.env`:** Edit the `.env` file in the `/home/ubuntu/symbiote-ceo-agent/` directory on your VM.
    ```bash
    nano /home/ubuntu/symbiote-ceo-agent/.env
    ```
    -   Set `N8N_API_KEY` to an API key generated within n8n (Settings -> API Keys). This key will allow your Python agent system to trigger n8n workflows programmatically.
    -   Verify `OLLAMA_BASE_URL` is `http://ollama:11434` (as defined in `docker-compose.yml` for inter-container communication).
    -   Verify `N8N_BASE_URL` is `http://n8n:5678` (as defined in `docker-compose.yml`).
    -   Optionally, change `OLLAMA_MODEL` to `mistral` if you pulled that model instead of `llama3`.
    -   Set `DAILY_REPORT_RECIPIENT_EMAIL` to your email address to receive daily reports from the CEO agent.

2.  **Restart Agent Container:** After modifying `.env`, restart the `symbiote-ceo-agent` container to load the new environment variables:
    ```bash
    cd /home/ubuntu/symbiote-ceo-agent
    docker-compose restart symbiote-ceo-agent
    ```

## 6. Running the System

### Manual Execution via CLI

You can interact with the agent system directly via its command-line interface (CLI) for testing or specific tasks.

1.  **Access the agent container's shell:**
    ```bash
    docker exec -it symbiote-ceo-agent bash
    ```
2.  **Run the main script:**
    ```bash
    python main.py
    ```
    This will launch the CLI, allowing you to enter high-level goals for the CEO agent.

### Automated Scheduling with n8n

For 24/7 autonomous operation, you will schedule the execution of the `main.py` script (or specific agent tasks) using n8n's scheduling capabilities.

1.  **Create a new n8n workflow for scheduling:**
    -   In n8n, create a new blank workflow.
    -   Add a `Cron` node as the trigger. Configure it with the desired schedule (e.g., daily, weekly). Refer to `config/schedules.py` for example cron expressions.
    -   Add an `Execute Command` node (from the `Community Nodes` or `Shell` category, you might need to install it if not available by default) to execute the Python script inside the `symbiote-ceo-agent` Docker container.
        -   **Command:** `docker exec symbiote-ceo-agent python main.py` (or a more specific command to trigger a particular agent's task if you refactor `main.py` to accept arguments).
        -   Ensure the n8n user has permissions to execute `docker` commands on the host system, or configure the `Execute Command` node to run with appropriate privileges.
    -   Alternatively, you can create a dedicated webhook in n8n that triggers the agent system, and then use the `Cron` node to call that webhook.

    *Example Cron Schedule (from `config/schedules.py`):*
    -   `CEO_AGENT_REPORT`: `0 8 * * *` (Every day at 8 AM)
    -   `RESEARCH_AGENT_TRENDS`: `0 9 * * MON` (Every Monday at 9 AM)
    -   `CONTENT_STRATEGIST_PLANNING`: `0 10 * * MON` (Every Monday at 10 AM)

2.  **Activate the scheduling workflow.**

## 7. Customization

-   **Agents:** Modify agent roles, goals, backstories, and tools in the `/agents/` directory to refine their behavior.
-   **Tasks:** Adjust task descriptions, expected outputs, and tool usage in the `/tasks/` directory.
-   **Tools:** Implement new custom tools in the `/tools/` directory or modify existing `n8n_tool.py` to integrate with more n8n workflows or other services.
-   **Configuration:** Update `config/brand_guidelines.py` and `config/schedules.py` to match your business needs.
-   **n8n Workflows:** Customize the `.json` workflows in `/workflows/` to integrate with your specific social media accounts, email providers, and image generation services.
-   **LLM Model:** Change `OLLAMA_MODEL` in `.env` to use a different local LLM (e.g., `mistral`, `codellama`).

## 8. Troubleshooting

-   **Ollama not running:** Check `docker logs ollama` for errors. Ensure port `11434` is open on your VM.
-   **n8n not accessible:** Check `docker logs n8n`. Ensure port `5678` is open on your VM and in your OCI VCN security list.
-   **Agent system errors:** Check `docker logs symbiote-ceo-agent`. Ensure all environment variables in `.env` are correctly set.
-   **n8n workflow failures:** Check the execution history of the specific workflow in the n8n UI for detailed error messages.
-   **Docker permissions:** If you encounter `permission denied` errors with Docker, ensure your user is in the `docker` group and you've re-logged in or run `newgrp docker`.

## 9. Contributing

Contributions are welcome! Please feel free to fork the repository, make your changes, and submit a pull request.

## 10. License

This project is licensed under the MIT License - see the LICENSE file for details.
