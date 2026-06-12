from crewai import Task

class ContentStrategistTasks:
    def __init__(self, agent):
        self.agent = agent

    def plan_weekly_calendar(self, context):
        return Task(
            description=(
                "Based on the CEO's goals and Research Agent's trend reports, plan a weekly content calendar for all SymbioteSystems channels. "
                "Specify topics, target channels (TikTok, Instagram, Facebook, X, Threads, Pinterest, YouTube), and publication dates. "
                "Ensure alignment with brand niche (AI, automation, digital products, cybersecurity) and aesthetic (dark, high-contrast, geometric, classified/executive style)."
            ),
            expected_output=(
                "A detailed weekly content calendar in Markdown format, including:\n                - Week number and dates\n                - For each day: Topic, Primary Channel, Secondary Channels (if any), Proposed Post Type (e.g., carousel, short video, infographic), Key Message/Hook.\n                Example: \n                ```markdown\n                ## Week 1: June 3 - June 9, 2026\n\n                ### Monday, June 3\n                - **Topic:** The Rise of AI-Powered Cyber Threats\n                - **Primary Channel:** LinkedIn\n                - **Secondary Channels:** X, Facebook\n                - **Post Type:** Infographic/Carousel\n                - **Key Message/Hook:** \"Is your digital fortress ready for the next wave of AI attacks?\"\n                ```"
            ),
            agent=self.agent,
            context=context
        )

    def generate_post_ideas(self, context):
        return Task(
            description=(
                "Generate compelling post ideas for each item in the weekly content calendar. "
                "Ideas should be creative, engaging, and tailored to the specific channel and target audience (HNWIs, executives, entrepreneurs, digital marketers). "
                "Incorporate current trends identified by the Research Agent."
            ),
            expected_output=(
                "A list of 3-5 unique post ideas for each content calendar item, including a brief description, target audience appeal, and potential visual concepts. "
                "Example: \n                ```markdown\n                **Topic: The Rise of AI-Powered Cyber Threats (LinkedIn Infographic)**\n                - **Idea 1:** \"5 AI-Driven Cyber Threats HNWIs Can't Ignore\" - Focus on specific, high-impact scenarios.\n                - **Idea 2:** \"The AI Arms Race: Protecting Your Digital Assets\" - Emphasize proactive defense strategies.\n                ```"
            ),
            agent=self.agent,
            context=context
        )

    def write_captions_scripts_hooks(self, context):
        return Task(
            description=(
                "Write engaging captions, short video scripts, and powerful hooks for the approved post ideas. "
                "Maintain SymbioteSystems' brand voice (authoritative, insightful, slightly mysterious) and aesthetic. "
                "Ensure content is optimized for each social media platform's best practices."
            ),
            expected_output=(
                "For each post idea, provide:\n                - **Caption:** Optimized for the primary channel, including relevant hashtags and CTAs.\n                - **Hook:** A compelling opening line for videos or attention-grabbing text for static posts.\n                - **Script (if video):** A brief script outline for short-form video content (e.g., TikTok, Reels).\n                Example: \n                ```markdown\n                **Post: AI-Powered Cyber Threats Infographic**\n                - **Caption (LinkedIn):** \"The digital landscape is evolving, and so are the threats. Our latest infographic breaks down the 5 AI-driven cyber threats that high-net-worth individuals and executives must be aware of. Protect your legacy. #Cybersecurity #AITrends #DigitalSecurity #HNWI\"\n                - **Hook (General):** \"Your digital assets are under attack from a new breed of intelligence.\"\n                ```"
            ),
            agent=self.agent,
            context=context
        )

    def maintain_brand_voice(self, context):
        return Task(
            description=(
                "Review all generated content (captions, scripts, hooks) to ensure strict adherence to SymbioteSystems' brand voice and aesthetic guidelines. "
                "Provide constructive feedback for any deviations."
            ),
            expected_output=(
                "A confirmation that content aligns with brand guidelines, or specific feedback on areas needing adjustment. "
                "Example: \"Content reviewed and approved. Brand voice is consistent.\" or \"Feedback: Adjust tone in paragraph 2 to be more authoritative.\""
            ),
            agent=self.agent,
            context=context
        )
