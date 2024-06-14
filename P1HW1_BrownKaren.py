# Karen Brown
 # June 14, 2024
 # P1HW1_BrownKaren

 # This program will allow the user to enter in an integer as a base and an integer as an exponent. It will then print the results.
 # This program will also allow the user to enter in 3 integers. The first 2 will be added together and the last one subtracted from that total. It will then print the results
 # Print a heading for the first equation: -----Calculating Exponents------ 
 # Allow the user to enter an input for Enter the integer as the base value, assign it to the variable base_value and convert it to an int
 # Allow the user to enter an input as the exponent, assign it to the variable exponent and convert it to an int
 # create a variable called result that holds the expression base_alue ** exponent
 # Print the the result to show base_value raised to the power of exponent is result !!!
 # Print a heading for the second equation: -----Addition and Subtraction----
 # Allow user to enter an integer and assign it to the variable start_int, convert it to an int
 # Allow user to enter an integer and assign it to the vairable add_int, convert it to an int
 # Allow user to enter an integer and assign it to the variable sub_int, convert it to an int
 # Print the results to show start_int + add_int - sub_int is equal to result

print()
print("-----Calculating Exponents----")
print()
print()
base_value = int(input("Enter an integer as the base value: "))
exponent = int(input("Enter an integer as the exponent: ")) 
print()
print()
print(base_value, "raised to the power of", exponent, "is", base_value**exponent, "!!")

print()
print()
print("-----Addition and Subtraction----")
print()
print()
start_int = int(input("Enter a starting integer: "))
add_int = int(input("Enter an integer to add: "))
sub_int = int(input("Enter an integer to subtract: "))
print()
print()
print(start_int, "+", add_int, "-", sub_int, "is equal to", start_int + add_int - sub_int)
