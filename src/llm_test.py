import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
print("\n" + GEMINI_API_KEY)
genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")
company = input("Name of company you want to study: ")
response = model.generate_content(f"Study the company {company} existing market")
print(response.text)
response = model.generate_content(
    f"simulate a couple future customer profiles for {company}"
)
print(response.text)
