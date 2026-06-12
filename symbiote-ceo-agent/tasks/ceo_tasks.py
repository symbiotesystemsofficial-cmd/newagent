from crewai import Task
from tools.n8n_tool import SendEmailTool

class CEOTasks:
    def __init__(self, agent):
        self.agent = agent

    def define_quarterly_goals(self, context):
        return Task(
            description=(
                "Define high-level quarterly goals for SymbioteSystems based on market analysis and product performance. "
                "These goals should drive overall business growth and align with the brand\'s niche (AI, automation, digital products, cybersecurity)."
            ),
            expected_output=(
                "A clear, concise list of 3-5 quarterly business goals, each with measurable objectives. "
                "Example: \'Increase \'The AI Fraud Survival Manual\' sales by 15% through targeted LinkedIn campaigns and content marketing.\'"
            ),
            agent=self.agent,
            context=context
        )

    def delegate_tasks(self, context):
        return Task(
            description=(
                "Break down the defined quarterly goals into actionable tasks and delegate them to the appropriate sub-agents. "
                "Ensure each sub-agent receives clear instructions and expected outcomes."
            ),
            expected_output=(
                "A structured delegation plan, specifying which sub-agent is responsible for which task, along with deadlines and success metrics. "
                "Example: \'Content Strategist: Develop 4 weeks of content around AI Fraud, due by [date].\'"
            ),
            agent=self.agent,
            context=context
        )

    def monitor_progress(self, context):
        return Task(
            description=(
                "Monitor the progress of all delegated tasks, identify any bottlenecks or underperforming areas, and provide guidance or re-delegation as needed. "
                "Ensure all agents are working efficiently towards the quarterly goals."
            ),
            expected_output=(
                "A weekly progress report summarizing the status of all tasks, highlighting achievements, challenges, and proposed adjustments. "
                "Example: \'Content creation for Q1 is 70% complete, Research Agent identified new trend for Q2 content.\'"
            ),
            agent=self.agent,
            context=context
        )

    def compile_daily_report(self, context):
        return Task(
            description=(
                "Compile a daily executive summary of all agent activities, key achievements, and any critical issues. "
                "This report should be concise and informative, suitable for stakeholders."
            ),
            expected_output=(
                "A daily report in Markdown format, summarizing the day\'s operations, key metrics (e.g., new followers, sales leads), and next steps. "
                "This report should be ready to be sent via email using the SendEmailTool."
            ),
            agent=self.agent,
            context=context,
            tools=[SendEmailTool()] # Assuming SendEmailTool is a defined tool
        )
