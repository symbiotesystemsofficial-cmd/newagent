import os
import requests
from crewai_tools import BaseTool
from dotenv import load_dotenv

load_dotenv()

N8N_BASE_URL = os.getenv("N8N_BASE_URL")
N8N_API_KEY = os.getenv("N8N_API_KEY")

class N8nWebhookTool(BaseTool):
    name: str
    description: str
    workflow_webhook_path: str # The specific path for the n8n webhook (e.g., 'send-email-webhook')

    def _run(self, **kwargs) -> str:
        if not N8N_BASE_URL or not N8N_API_KEY:
            return "Error: N8N_BASE_URL or N8N_API_KEY not set in environment variables."

        webhook_url = f"{N8N_BASE_URL}/webhook/{self.workflow_webhook_path}"

        headers = {
            "Content-Type": "application/json",
            "X-N8N-API-KEY": N8N_API_KEY # For n8n API calls, if needed. Webhooks usually don't need this.
        }

        payload = kwargs

        try:
            response = requests.post(webhook_url, json=payload, headers=headers)
            response.raise_for_status() # Raise an exception for HTTP errors
            return f"n8n workflow '{self.workflow_webhook_path}' triggered successfully. Response: {response.text}"
        except requests.exceptions.RequestException as e:
            return f"Error triggering n8n workflow '{self.workflow_webhook_path}': {e}"


class SendEmailTool(N8nWebhookTool):
    name: str = "Send Email Tool"
    description: str = "Sends an email using a predefined n8n workflow. Input: recipient (str), subject (str), body (str)."
    workflow_webhook_path: str = "send-email"

    def _run(self, recipient: str, subject: str, body: str) -> str:
        return super()._run(recipient=recipient, subject=subject, body=body)

class PostSocialMediaTool(N8nWebhookTool):
    name: str = "Post Social Media Tool"
    description: str = "Posts content to a specified social media platform using a predefined n8n workflow. Input: platform (str), content (str), image_url (str, optional)."
    workflow_webhook_path: str = "post-social-media"

    def _run(self, platform: str, content: str, image_url: str = None) -> str:
        return super()._run(platform=platform, content=content, image_url=image_url)

class GenerateImageTool(N8nWebhookTool):
    name: str = "Generate Image Tool"
    description: str = "Generates an image based on a prompt using a predefined n8n workflow (e.g., integrating with a local image generation model). Input: prompt (str), style (str, optional)."
    workflow_webhook_path: str = "generate-image"

    def _run(self, prompt: str, style: str = None) -> str:
        return super()._run(prompt=prompt, style=style)

class WebScrapeTool(N8nWebhookTool):
    name: str = "Web Scrape Tool"
    description: str = "Scrapes content from a given URL using a predefined n8n workflow. Input: url (str), selector (str, optional)."
    workflow_webhook_path: str = "web-scrape"

    def _run(self, url: str, selector: str = None) -> str:
        return super()._run(url=url, selector=selector)

# Instantiate tools for use in agents
send_email_tool = SendEmailTool()
post_social_media_tool = PostSocialMediaTool()
generate_image_tool = GenerateImageTool()
web_scrape_tool = WebScrapeTool()
