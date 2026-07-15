import os

from dotenv import load_dotenv
from groq import Groq

from smart_repo.services.prompt_builder import PromptBuilder

load_dotenv()


class AIService:
    """
    Handles communication with the Groq LLM.
    """

    def __init__(self):

        self.client = Groq(
            api_key=os.getenv("GROQ_API_KEY")
        )

        self.prompt_builder = PromptBuilder()

    def ask(self, question: str) -> str:
        """
        Ask the repository-aware AI assistant.
        """

        prompt = self.prompt_builder.build(question)

        response = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            temperature=0.2,
            max_tokens=1024,
        )

        return response.choices[0].message.content