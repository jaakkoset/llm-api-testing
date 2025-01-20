from app import LLM

user_prompt = input("Name of company you want to study: ")
llm = LLM()

response = llm.generate_response(user_prompt)
print(response)
