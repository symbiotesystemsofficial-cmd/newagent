from crewai import Task
from tools.n8n_tool import WebScrapeTool

class ResearchTasks:
    def __init__(self, agent):
        self.agent = agent

    def monitor_industry_trends(self):
        return Task(
            description=(
                "Continuously monitor the latest trends, news, and breakthroughs in AI, automation, and cybersecurity. "
                "Focus on developments relevant to HNWIs, executives, entrepreneurs, and digital marketers. "
                "Use web scraping tools (via n8n) to gather information from reputable sources."
            ),
            expected_output=(
                "A concise summary of the top 3-5 most significant industry trends identified in the past week, "
                "including their potential impact on SymbioteSystems and its target audience. "
                "Example: \'Trend: Rise of AI-powered phishing attacks targeting C-suite executives. Impact: Increased demand for advanced digital security education.\'"
            ),
            agent=self.agent,
            tools=[WebScrapeTool()] # Assuming WebScrapeTool is a defined tool
        )

    def track_competitor_activity(self):
        return Task(
            description=(
                "Identify and track the activities of key competitors in the digital security and productivity ecosystem space. "
                "Analyze their content strategies, product launches, marketing campaigns, and audience engagement. "
                "Focus on competitors targeting similar high-value audiences."
            ),
            expected_output=(
                "A brief report on competitor activities, highlighting any new strategies, successful campaigns, or product offerings. "
                "Include insights on what SymbioteSystems can learn or adapt. "
                "Example: \'Competitor X launched a new webinar series on data privacy, gaining significant traction. Suggest SymbioteSystems consider similar educational content.\'"
            ),
            agent=self.agent,
            tools=[WebScrapeTool()] # Assuming WebScrapeTool is a defined tool
        )

    def find_viral_content_patterns(self):
        return Task(
            description=(
                "Analyze social media platforms and content aggregators to identify viral content patterns, formats, and topics "
                "that resonate with the target audience (HNWIs, executives, entrepreneurs, digital marketers). "
                "Look for trends in engagement, shares, and comments across TikTok, Instagram, Facebook, X, Threads, Pinterest, and YouTube."
            ),
            expected_output=(
                "A report detailing current viral content patterns, including examples, reasons for their success, and suggestions for how SymbioteSystems can adapt these patterns. "
                "Example: \'Short-form video explainers on complex cybersecurity topics are performing well on TikTok. Suggest creating 60-second animated explainers.\'"
            ),
            agent=self.agent,
            tools=[WebScrapeTool()] # Assuming WebScrapeTool is a defined tool
        )

    def compile_trend_reports(self, context):
        return Task(
            description=(
                "Compile all gathered information on industry trends, competitor activities, and viral content patterns into a comprehensive trend report for the Content Strategist Agent. "
                "The report should be actionable and provide clear recommendations."
            ),
            expected_output=(
                "A well-structured trend report in Markdown format, summarizing key findings and offering specific content and marketing recommendations. "
                "Example: \'Weekly Trend Report: AI-powered cyber threats are a major concern. Recommend content focusing on proactive defense and expert interviews.\'"
            ),
            agent=self.agent,
            context=context
        )
