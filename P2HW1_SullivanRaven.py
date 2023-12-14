#09/18/2023
#CTI-110 P2HW1
#Raven Sullivan
#
print("This program calculates and displays travel expenses.\n")
budget = float(input("Enter Budget: "))
print()

destination = input("Enter your travel destination: ")
print()

gas = float(input("How much do you think you will spend on gas?"))
print()

hotel = float(input("Aproximately, how much will you need for accomodation/hotel"))
print()

food = float(input("Last, how much do you need for food "))
expenses = gas + hotel + food

balance = budget - expenses
print("\-----------Travel Expenses-----------")
print("Location:",destination)
print("Initial Budget:" + "$",budget)
print("\nFuel" + "$",gas)
print("Accomodation:" + "$",hotel)
print("Food" + "$",food)
print("\nRemaining Balance:" + "$",balance)
