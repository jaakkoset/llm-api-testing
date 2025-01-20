from app import Gemini

user_prompt = input("Name of company you want to study: ")
llm = Gemini(user_prompt)

response = llm.get_llm_response()
print(response)
