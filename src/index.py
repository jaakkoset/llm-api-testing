from app import Simulator

while True:
    company = input("Name of company you want to study: ")
    print("\nSimulating three customers...\n")
    simulator = Simulator()

    response = simulator.simulate_customers(company)
    print(response)
