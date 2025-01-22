from app import LLM

company = input("Name of company you want to study: ")
print("\nSimulating three customers...\n")
llm = LLM()

response = llm.simulate_customers(company)
print(response)
