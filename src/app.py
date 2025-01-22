from gemini import Gemini


class LLM:
    def __init__(self, llm=Gemini()):
        self.llm = llm

    def simulate_customers(self, company) -> str:
        """Returns descriptions for three simulated customers for the given company"""
        company_is_valid = self.company_is_valid(company)
        print(company_is_valid)
        prompt = f"simulate three future customer profiles for {company}"
        return self.llm.get_response(prompt)

    def company_is_valid(self, company) -> bool:
        """Asks Gemini if it is comfortable with creating user profiles for the given
        company. Raises ValueError if the answer is unclear.

        Returns
        -------
            True or False"""
        prompt = (
            f"Would you say you have enough information about the company {company} "
            f"to create simulated user profiles for it? Please answer only YES or NO"
        )
        response = self.llm.get_response(prompt)
        return response
