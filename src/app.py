import os
from dotenv import load_dotenv
import google.generativeai as genai


class Gemini:
    def __init__(self, user_prompt):
        self.user_prompt = user_prompt
        self.GEMINI_API_KEY = self.__load_key()
        self.ai_model = self.__configure_ai()

    def __load_key(self):
        load_dotenv()
        return os.getenv("GEMINI_API_KEY")

    def __configure_ai(self):
        genai.configure(api_key=self.GEMINI_API_KEY)
        return genai.GenerativeModel("gemini-1.5-flash")

    def get_llm_response(self):
        response1 = self.ai_model.generate_content(
            f"Study the existing market of the company {self.user_prompt} in a few points"
        )
        response2 = self.ai_model.generate_content(
            f"simulate three future customer profiles for {self.user_prompt}"
        )
        response = ""
        response += response1.text
        response += "\n\n"
        response += response2.text
        return response
