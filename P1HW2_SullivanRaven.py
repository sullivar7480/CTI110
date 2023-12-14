#This Program Calculates and Displays Travel Expenses
#/09/05/2023
#CTI-110-P1HW2 - Travel Expense
#

print("This program calculates and displays travel expenses.\n")
budget = float(input("Enter Budget: "))
print()

destination = input("enter your travel destination: ")
print()

gas = float(input("How much do you think you will spend on gas? "))
print()

hotel = float(input("Approximately, how much will you need for accomataion/hotel? "))
print()

food = float(input("Last, how much do you need for food?"))
print()

expenses = gas + hotel + food
balance = budget - expenses
print("\n-----------Travel Expenses-----------")
print("Loacation",destination)
print("Initial Budget:",budget)
print("Accomodation:",hotel)
print("Food",food)
print("\nRemaining Balance:",balance)
