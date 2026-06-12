from crewai import Task
from tools.n8n_tool import SendEmailTool, WebScrapeTool

class SalesMarketingTasks:
    def __init__(self, agent):
        self.agent = agent

    def manage_product_promotion_cycles(self, product_name: str, launch_date: str, duration_weeks: int):
        return Task(
            description=(
                f"Plan and manage the promotion cycle for {product_name}, starting on {launch_date} and lasting for {duration_weeks} weeks. "
                "This includes defining key milestones, promotional channels, and target audience segments. "
                "Focus on products like \'The AI Fraud Survival Manual\' and \'The Ultimate Agency OS\'."
            ),
            expected_output=(
                "A detailed promotion plan in Markdown format, outlining:\n                - Product name and promotion dates\n                - Key promotional phases (e.g., pre-launch, launch, post-launch)\n                - Marketing channels to be utilized (e.g., email, social media ads, partnerships)\n                - Target audience segments for each phase."
            ),
            agent=self.agent,
            # tools=[] # Tools will be added in a later phase
        )

    def write_email_sequences(self, campaign_name: str, product_name: str, target_audience: str):
        return Task(
            description=(
                f"Develop a compelling email sequence for the '{campaign_name}' campaign, promoting '{product_name}' to '{target_audience}'. "
                "The sequence should include welcome emails, educational content, testimonials, and clear calls-to-action. "
                "Maintain SymbioteSystems' brand voice and aesthetic."
            ),
            expected_output=(
                "A complete email sequence (3-5 emails) in Markdown format, including:\n                - Subject lines\n                - Email body content\n                - Calls-to-Action (CTAs)\n                - Suggested send schedule."
            ),
            agent=self.agent,
            tools=[SendEmailTool()] # Assuming SendEmailTool is a defined tool
        )

    def optimize_ctas_funnels(self, current_cta: str, current_funnel_stage: str):
        return Task(
            description=(
                f"Analyze the effectiveness of the current Call-to-Action '{current_cta}' and the '{current_funnel_stage}' stage of the sales funnel. "
                "Suggest improvements to increase conversion rates. "
                "This might involve A/B testing different CTAs, refining landing page copy, or streamlining the user journey."
            ),
            expected_output=(
                "A report in Markdown format detailing:\n                - Analysis of current CTA/funnel performance\n                - Proposed optimizations with rationale\n                - Expected impact on conversion rates."
            ),
            agent=self.agent,
            # tools=[] # Tools will be added in a later phase
        )

    def track_conversion_metrics(self, campaign_id: str):
        return Task(
            description=(
                f"Track and report on conversion metrics for the campaign with ID '{campaign_id}'. "
                "This includes monitoring lead generation, sales conversions, customer acquisition cost, and return on ad spend. "
                "Use n8n to integrate with analytics platforms if necessary."
            ),
            expected_output=(
                "A comprehensive conversion metrics report in Markdown format, including:\n                - Key performance indicators (KPIs) for the campaign\n                - Trends and insights\n                - Recommendations for future campaigns."
            ),
            agent=self.agent,
            tools=[WebScrapeTool()] # Assuming n8n can be used to pull data from analytics platforms
        )
