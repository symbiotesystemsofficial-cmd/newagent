"""Entry point for the SymbioteSystems Autonomous CEO Multi-Agent System.

This script initializes the CrewAI agents, sets up the Ollama LLM and ChromaDB for memory,
and orchestrates the execution of tasks based on high-level goals.
It also provides a basic CLI for interaction.
"""

import os
import sys
from crewai import Crew, Process
from dotenv import load_dotenv
from langchain_community.llms import Ollama
from langchain.memory import ConversationBufferWindowMemory
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings

# Load environment variables from .env file
load_dotenv()

# --- Configuration --- #
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3")
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
CHROMADB_PATH = os.getenv("CHROMADB_PATH", "./chroma_db")

# --- Initialize LLM and Embeddings --- #
try:
    ollama_llm = Ollama(model=OLLAMA_MODEL, base_url=OLLAMA_BASE_URL)
    ollama_embeddings = OllamaEmbeddings(model=OLLAMA_MODEL, base_url=OLLAMA_BASE_URL)
except Exception as e:
    print(f"Error initializing Ollama: {e}. Please ensure Ollama is running and the model is pulled.")
    sys.exit(1)

# --- Initialize ChromaDB for memory persistence --- #
# Note: For a true persistent memory across runs, the ChromaDB instance needs to be loaded
# and passed to the agents/crew. CrewAI handles this internally if memory=True.
# The vectorstore here is primarily for embeddings if tools need it directly.
vectorstore = Chroma(persist_directory=CHROMADB_PATH, embedding_function=ollama_embeddings)

# --- Import Agent creation functions --- #
from agents.ceo_agent import create_ceo_agent
from agents.content_strategist_agent import create_content_strategist_agent
from agents.research_agent import create_research_agent
from agents.social_media_manager_agent import create_social_media_manager_agent
from agents.sales_marketing_agent import create_sales_marketing_agent
from agents.design_agent import create_design_agent

# --- Import Task classes --- #
from tasks.ceo_tasks import CEOTasks
from tasks.content_strategist_tasks import ContentStrategistTasks
from tasks.research_tasks import ResearchTasks
from tasks.social_media_manager_tasks import SocialMediaManagerTasks
from tasks.sales_marketing_tasks import SalesMarketingTasks
from tasks.design_tasks import DesignTasks

# --- Instantiate Agents --- #
ceo_agent = create_ceo_agent(ollama_llm)
content_strategist_agent = create_content_strategist_agent(ollama_llm)
research_agent = create_research_agent(ollama_llm)
social_media_manager_agent = create_social_media_manager_agent(ollama_llm)
sales_marketing_agent = create_sales_marketing_agent(ollama_llm)
design_agent = create_design_agent(ollama_llm)

# --- Initialize Task instances for each agent --- #
ceo_tasks = CEOTasks(ceo_agent)
content_strategist_tasks = ContentStrategistTasks(content_strategist_agent)
research_tasks = ResearchTasks(research_agent)
social_media_manager_tasks = SocialMediaManagerTasks(social_media_manager_agent)
sales_marketing_tasks = SalesMarketingTasks(sales_marketing_agent)
design_tasks = DesignTasks(design_agent)

class SymbioteSystemsCrew:
    def __init__(self):
        self.ceo_agent = ceo_agent
        self.content_strategist_agent = content_strategist_agent
        self.research_agent = research_agent
        self.social_media_manager_agent = social_media_manager_agent
        self.sales_marketing_agent = sales_marketing_agent
        self.design_agent = design_agent

    def run_crew(self, high_level_goal: str):
        print(f"\n## SymbioteSystems Autonomous CEO System - Executing Goal: {high_level_goal}")
        print("---------------------------------------------------")

        # The CEO agent's primary task is to define and delegate based on the high-level goal.
        # This is a simplified example. In a more complex system, the CEO would dynamically
        # create and assign tasks to sub-agents based on its understanding of the goal.
        # For now, we'll use a predefined set of tasks that the CEO orchestrates.

        # CEO Agent defines quarterly goals (simplified to the current high_level_goal for this run)
        define_goals_task = ceo_tasks.define_quarterly_goals(context=high_level_goal)

        # Example of a simplified task flow for a content campaign
        # In a real scenario, the CEO would dynamically generate these tasks.
        content_plan_task = content_strategist_tasks.plan_weekly_calendar(context=f"Plan content based on the goal: {high_level_goal}")
        post_ideas_task = content_strategist_tasks.generate_post_ideas(context=content_plan_task)
        captions_scripts_task = content_strategist_tasks.write_captions_scripts_hooks(context=post_ideas_task)

        monitor_trends_task = research_tasks.monitor_industry_trends()
        track_competitors_task = research_tasks.track_competitor_activity()

        # Social Media Manager tasks - assuming content is ready from Content Strategist
        publish_content_task = social_media_manager_tasks.schedule_and_publish_posts(
            content_plan="Content for the current campaign, focusing on relevant platforms.",
            image_urls={}
        )

        email_sequence_task = sales_marketing_tasks.write_email_sequences(
            campaign_name="Current Campaign",
            product_name="SymbioteSystems Products",
            target_audience="HNWIs and Executives"
        )

        design_graphic_task = design_tasks.create_social_media_graphics(
            content_description="Visuals for the current campaign",
            platform="General",
            graphic_type="Social Media Graphic"
        )

        # The Crew Definition
        crew = Crew(
            agents=[
                self.ceo_agent,
                self.content_strategist_agent,
                self.research_agent,
                self.social_media_manager_agent,
                self.sales_marketing_agent,
                self.design_agent
            ],
            tasks=[
                define_goals_task,
                content_plan_task,
                post_ideas_task,
                captions_scripts_task,
                monitor_trends_task,
                track_competitors_task,
                publish_content_task,
                email_sequence_task,
                design_graphic_task
            ],
            process=Process.hierarchical, # Use hierarchical process for CEO delegation
            manager_llm=ollama_llm, # CEO agent will use this LLM for orchestration
            memory=True, # Enable memory for the crew
            verbose=True
        )

        result = crew.kickoff()
        print("\n\n########################")
        print("## Crew Work Completed!")
        print("########################")
        print(result)

        # CEO Agent compiles daily report (this would be a separate scheduled task)
        # For demonstration, we'll just print a placeholder.
        print("\n\n## Daily Report Placeholder:")
        print("The CEO agent would now compile a daily report based on the crew's activities.")
        # In a real system, this would involve another task and tool call to send an email.
        # ceo_tasks.compile_daily_report(context=result).execute()

    def cli_interface(self):
        while True:
            print("\n--- SymbioteSystems CEO Agent CLI ---")
            print("1. Run a new high-level goal")
            print("2. Check agent status (placeholder)")
            print("3. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                goal = input("Enter the high-level goal for the CEO agent: ")
                if goal:
                    self.run_crew(goal)
                else:
                    print("Goal cannot be empty.")
            elif choice == '2':
                print("Agent status check is a placeholder. In a real system, this would query agent logs or a monitoring service.")
            elif choice == '3':
                print("Exiting CLI. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    print("Initializing SymbioteSystems CEO Agent System...")
    symbiote_crew = SymbioteSystemsCrew()
    symbiote_crew.cli_interface()
