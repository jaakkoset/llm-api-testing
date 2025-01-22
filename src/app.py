from gemini import Gemini


class LLM:
    def __init__(self, llm=Gemini()):
        self.llm = llm

    def simulate_customers(self, company) -> str:
        """Returns descriptions for three simulated customers for the given company"""
        prompt = f"simulate three future customer profiles for {company}"
        return self.llm.get_response(prompt)
