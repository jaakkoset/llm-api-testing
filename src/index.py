from app import LLM

user_prompt = input("Name of company you want to study: ")
llm = LLM(user_prompt)

response = llm.generate_response()
print(response)
