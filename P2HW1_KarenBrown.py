 # Karen Brown
 # June 22, 2024
 # P2HW1
 # General Discription
     #This program will work the same as P1HW2, however the output will be formated differently.
 # Detailed Description
     #Obtain the following input from the user, and assign it to the corresponding variables
     #    budget (convert this to an int)
     #    destination
     #    gas (convert this to an int)
     #    accommodations (convert this to an int)
     #    food (convert this to an int)
     # add the expenses(fuel, accommodations, food) and subtract it the initial budget, assign it to the variable rem_bal
     # Print the following under the headline Travel Expenses to appear as two columns(the description and the users input). Money values should appear as floats with $ signs.
     #    location: 
     #    initial budget:
     #    fuel:
     #    accommodation:
     #    food:
     # print the remaining balance

#print the description of the program
print("\nThis program calculates and displays travel expenses")

#receive input from the user
budget = int(input("\nEnter Budget: "))
destination = input("\nEnter your travel destination: ")
gas = int(input("\nHow much do you think you will spend on gas? "))
accommodations = int(input("\nApproximately, how much will you need for accommodation/hotel? "))
food = int(input("\nLast, how much do you need for food? "))

#find the remaining balance
remaining_bal = budget - (gas + accommodations + food)

#print a headline 
print("\n------------Travel Expenses------------")

#print the users travel expenses and destination
print(f"{'Location:':<21}{destination}")
print(f"{'Initial Budget:':<20} ${budget:.2f}")
print(f"{'Fuel:':<20} ${gas:.2f}")
print(f"{'Accomodation:':<20} ${accommodations:.2f}")
print(f"{'Food:':<20} ${food:.2f}")
print("---------------------------------------")

#print the remaining balance after the users expenses are paid
print(f"\n{'Remaining Balance:':<20} ${remaining_bal:.2f}")
