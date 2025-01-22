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
        answer = self.parse_yes_no_answer(response)
        return answer

    def parse_yes_no_answer(self, answer) -> bool:
        """Determine whether Gemini answered YES or NO. Raise ValueError if the answer
        is something else

        Returns
        -------
            True if answer is YES and False if it is NO"""
        answer = answer.replace("\n", "")
        if answer == "YES":
            return True
        if answer == "NO":
            return False
        raise ValueError("Gemini should have answered YES or NO. It aswered", answer)
