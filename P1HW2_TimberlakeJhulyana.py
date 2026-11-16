 # Jhulyana Timberlake
 # 11/01/2026
 # P1HW2
 # This Program calculates and displays travel expenses

# Ask the user for their budget and destination
budget = int(input("Enter Budget: "))
destination = input("Enter travel destination: ")
# Ask the user for their travel expenses
gas_money = int(input("How much do you think you will spend on gas? "))
hotel_expenses = int(input("Approximately, how much will you need for accommodation/hotel? "))
food_expenses = int(input("Last, how much do you need for food? "))
# Add all expenses together
Total_expenses = gas_money + hotel_expenses + food_expenses
# Subtract expenses from the budget
remaining_budget = budget - (gas_money + hotel_expenses + food_expenses)
# Display the results
print()
print("----------Travel Expenses----------")
print("Location:", destination)
print("Initial Budget:", budget)
print()
print("Fuel:", gas_money)
print("Accomodation:", hotel_expenses)
print("Food:", food_expenses)
print()
print("Remaining Balance:", remaining_budget)