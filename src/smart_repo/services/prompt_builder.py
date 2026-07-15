from smart_repo.services.context_builder import ContextBuilder


class PromptBuilder:
    """
    Build a structured prompt for the LLM.
    """

    SYSTEM_PROMPT = """
You are Smart-Repo, an AI software engineering assistant.

Your job is to answer questions ONLY using the repository context provided.

Rules:
- Never invent information.
- If the answer is not present in the repository, clearly say so.
- Explain code in a concise and technical manner.
- Mention file names whenever possible.
- Prefer architecture explanations over code repetition.
"""

    def __init__(self):
        self.context_builder = ContextBuilder()

    def build(self, question: str) -> str:
        """
        Build the final LLM prompt.
        """

        context = self.context_builder.build(question)

        prompt = f"""
===========================
SYSTEM
===========================

{self.SYSTEM_PROMPT}

===========================
REPOSITORY CONTEXT
===========================

{context}

===========================
USER QUESTION
===========================

{question}

===========================
ANSWER
===========================
"""

        return prompt.strip()