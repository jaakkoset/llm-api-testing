import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")

company = input("Name of company you want to study: ")
response = model.generate_content(
    f"Study the existing market of the company {company} in a few points"
)
print(response.text)
response = model.generate_content(
    f"simulate three future customer profiles for {company}"
)
print("\n\n")
print(response.text)
