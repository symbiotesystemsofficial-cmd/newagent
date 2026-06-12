from crewai import Task
from tools.n8n_tool import PostSocialMediaTool

class SocialMediaManagerTasks:
    def __init__(self, agent):
        self.agent = agent

    def schedule_and_publish_posts(self, content_plan: str, image_urls: dict = None):
        return Task(
            description=(
                "Schedule and publish content across all SymbioteSystems social media channels "
                "(TikTok, Instagram, Facebook, X, Threads, Pinterest, YouTube) based on the provided content plan. "
                "Utilize n8n for automated posting. Ensure correct captions, hashtags, and visuals are used."
            ),
            expected_output=(
                "Confirmation of successful scheduling/publishing for each post, including platform and timestamp. "
                "Example: \'Post for Instagram scheduled for 2026-06-01 10:00 AM. Post for X published.\'"
            ),
            agent=self.agent,
            tools=[PostSocialMediaTool()],
            context=[content_plan, image_urls]
        )

    def monitor_engagement(self):
        return Task(
            description=(
                "Monitor engagement metrics (likes, comments, shares, saves) across all social media platforms. "
                "Identify high-performing content and areas for improvement. "
                "Provide a summary of engagement trends."
            ),
            expected_output=(
                "A weekly engagement report in Markdown format, summarizing key metrics for each platform, "
                "highlighting top-performing posts, and identifying any significant changes in audience interaction. "
                "Example: \'Instagram saw a 15% increase in likes this week, with the AI Fraud infographic being the top post.\'"
            ),
            agent=self.agent,
            # tools=[N8nTool().get_social_media_analytics] # Assuming a tool for analytics retrieval via n8n
        )

    def respond_to_comments_dms(self):
        return Task(
            description=(
                "Actively respond to comments and direct messages on all social media channels. "
                "Maintain SymbioteSystems\' brand voice and provide helpful, engaging, and professional responses. "
                "Escalate complex inquiries to the CEO agent if necessary."
            ),
            expected_output=(
                "A daily summary of interactions, including types of comments/DMs received, responses provided, and any escalated issues. "
                "Example: \'Responded to 10 comments on Instagram, 3 DMs on X. Escalated one product inquiry to CEO.\'"
            ),
            agent=self.agent,
            # tools=[N8nTool().monitor_social_media_inbox] # Assuming a tool for monitoring social media inboxes via n8n
        )

    def track_analytics(self, context):
        return Task(
            description=(
                "Compile and analyze social media analytics to track growth, reach, and audience demographics. "
                "Generate insights to inform future content strategy and identify opportunities for optimization."
            ),
            expected_output=(
                "A monthly social media analytics report in Markdown format, detailing follower growth, reach, impressions, "
                "engagement rates, and audience demographic shifts across all platforms. "
                "Provide actionable recommendations for the Content Strategist. "
                "Example: \'Monthly Report: Overall follower growth of 5%. TikTok engagement is highest among 25-34 age group. Recommend more short-form content for this demographic.\'"
            ),
            agent=self.agent,
            context=context
            # tools=[N8nTool().get_social_media_analytics] # Assuming a tool for analytics retrieval via n8n
        )
