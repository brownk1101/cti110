# Karen Brown
 # June 18, 2024
 # P2LAB2
 # Brief description
     # This program will use a dictionary to display the MPG of some vehicles and how much gas is needed to go a specified distance in that vehicle
 #Detailed description
     #create a dictionary called vehicle for the following keys and their value
     #{Camaro: 18.21, Prius: 52.36, Model S: 110, Silverado: 26}
     #create a list, keys, to hold the keys for this dictionary
     #print keys list
     #prompt the user to enter a vehicle from the keys list, assigning it to the variable vehicle_name
     #print the MPG for that vehicle
     #receive input from the user for how many miles they will drive the vehicle, assign this to the variable miles_driving
     #calculate the amount of gas needed, in gallons, to drive the vehicle they chose the given number of miles
     #use the expression miles_driving/vehicle_mpg
     #print the gallons of gas needed, rounded to 2 decimal places

vehicle = {"Camaro": 18.21, "Prius": 52.36, "Model S": 110, "Silverado": 26}
vehicle_keys = vehicle.keys()
print(vehicle_keys)
vehicle_name = input("\nEnter a vehicle to see it's mpg: ")
vehicle_mpg = vehicle[vehicle_name]
print(f"\nThe {vehicle_name} gets {vehicle_mpg} mpg.")
miles_driving = float(input(f"\nHow many miles will you drive the {vehicle_name}? "))
gallons_needed = miles_driving/vehicle_mpg
print(f"\n{gallons_needed:.2f} gallon(s) of gas are needed to drive the {vehicle_name} {miles_driving} miles.")

