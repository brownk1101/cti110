 # Karen Brown
 # June, 14, 2024 
 # P1HW2
 # This program will obtain information from the user to calculate and display travel expenses.
 # It will factor in the users budget and expenses and will return the users balance.
 # Obtain the following input from the user, and assign it to the corresponding variables
 #    budget (convert this to an int)
 #    destination
 #    gas (convert this to an int)
 #    accommodations (convert this to an int)
 #    food (convert this to an int)
 # add the expenses(fuel, accommodations, food) and subtract it the initial budget, assign it to the variable rem_bal
 # Print the following under the headline Travel Expenses
 #    location, initial budget, fuel, accommodation, food
 # print the remaining balance

print()
print("This program calculates and displays travel expenses")
print()
budget = int(input("Enter Budget: "))
print()
destination = input("Enter your travel destination: ")
print()
gas = int(input("How much do you think you will spend on gas? "))
print()
accommodations = int(input("Approximately, how much will you need for accommodation/hotel? "))
print()
food = int(input("Last, how much do you need for food? "))
rem_bal = budget - (gas + accommodations + food)
print()
print("------------Travel Expenses------------")
print("Location:", destination)
print("Initial Budget:", budget)
print()
print("Fuel:", gas)
print("Accommodation:", accommodations)
print("Food:", food)
print()
print("Remaining Balance:", rem_bal)
