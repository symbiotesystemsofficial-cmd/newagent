from crewai import Agent
from dotenv import load_dotenv
import os
from tools.n8n_tool import WebScrapeTool

load_dotenv()

def create_research_agent(ollama_llm):
    return Agent(
        role=\'Research Agent\',
        goal=\'Continuously monitor industry trends, competitor activities, and viral content patterns to provide actionable insights for content and marketing strategies.\',
        backstory=(
            "This agent is the intelligence hub of SymbioteSystems. "
            "It tirelessly scours the internet for the latest developments in AI, automation, and cybersecurity, "
            "keeping a close watch on what competitors are doing and identifying emerging viral content. "
            "Its reports are crucial for the Content Strategist to generate relevant and engaging ideas, "
            "and for the Sales & Marketing Agent to refine product positioning. "
            "It ensures SymbioteSystems remains at the forefront of its niche by providing timely and accurate information."
        ),
        verbose=True,
        allow_delegation=False,
        llm=ollama_llm,
        tools=[WebScrapeTool()]
    )
