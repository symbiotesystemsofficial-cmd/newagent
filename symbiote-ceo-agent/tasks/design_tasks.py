from crewai import Task
from tools.n8n_tool import N8nTool

class DesignTasks:
    def __init__(self, agent):
        self.agent = agent

    def generate_carousel_images(self, topic: str, number_of_slides: int, key_messages: list):
        return Task(
            description=(
                f"Generate {number_of_slides} carousel images for a social media post on the topic: \'{topic}\'. "
                "Each slide should convey a key message from the provided list. "
                "Adhere to SymbioteSystems\' dark, high-contrast, geometric, classified/executive style aesthetic. "
                "Use the n8n tool to integrate with an image generation service."
            ),
            expected_output=(
                "A list of URLs to the generated carousel images, along with a brief description of each image\'s content. "
                "Example: \'[https://image1.com/url, https://image2.com/url]\'."
            ),
            agent=self.agent,
            tools=[N8nTool().generate_image]
        )

    def create_social_media_graphics(self, content_description: str, platform: str, graphic_type: str):
        return Task(
            description=(
                f"Create a social media graphic for \'{platform}\' based on the content description: \'{content_description}\'. "
                f"The graphic type is \'{graphic_type}\'. "
                "Ensure the graphic aligns with SymbioteSystems\' brand guidelines (colors, fonts, aesthetic). "
                "Use the n8n tool to integrate with an image generation service."
            ),
            expected_output=(
                "A URL to the generated social media graphic, along with a confirmation that it meets brand guidelines. "
                "Example: \'https://graphic.com/url - Graphic created and approved for brand consistency.\'."
            ),
            agent=self.agent,
            tools=[N8nTool().generate_image]
        )

    def maintain_brand_consistency(self, visual_asset_url: str, brand_guidelines: dict):
        return Task(
            description=(
                f"Review the visual asset at \'{visual_asset_url}\' against SymbioteSystems\' brand guidelines. "
                "Check for adherence to color palette, typography, geometric patterns, and overall classified/executive style. "
                "Provide feedback on any inconsistencies."
            ),
            expected_output=(
                "A confirmation that the visual asset is brand-consistent, or specific feedback on areas that need adjustment. "
                "Example: \'Visual asset is brand-consistent.\' or \'Feedback: Font used is not approved; please use Inter Bold.\'."
            ),
            agent=self.agent,
            # tools=[] # This task might not require external tools, but rather internal LLM reasoning based on provided guidelines.
        )
