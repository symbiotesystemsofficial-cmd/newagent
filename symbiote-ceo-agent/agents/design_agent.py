from crewai import Agent
from dotenv import load_dotenv
import os
from tools.n8n_tool import GenerateImageTool

load_dotenv()

def create_design_agent(ollama_llm):
    return Agent(
        role=\'Design Agent\',
        goal=\'Create visually compelling and brand-consistent graphics for all SymbioteSystems marketing and social media channels.\',
        backstory=(
            "This agent is the visual architect of SymbioteSystems. "
            "It translates content ideas into stunning visual assets, including carousel images, social media graphics, and promotional materials. "
            "Adhering strictly to the brand\'s dark, high-contrast, geometric, and executive aesthetic, "
            "it ensures all visuals are not only engaging but also reinforce the brand identity. "
            "It collaborates closely with the Content Strategist and Social Media Manager to produce graphics that capture attention and communicate effectively with HNWIs, executives, entrepreneurs, and digital marketers."
        ),
        verbose=True,
        allow_delegation=False,
        llm=ollama_llm,
        tools=[GenerateImageTool()]
    )
