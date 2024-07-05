#Karen Brown

 #June 5, 2024

 #P4LAB2

 #General Description
    #This program will show the multiplication table, 1-12, for integers 0 and greater
 #Detailed description
    #prime the play again variable with yes to initiate the program
    #begin the main loop as long as play_again does not equal no
        #get an integer from the user
        #if the integer is 0 or greater
            #begin the inner loop to run from numbers 1 to 12
                #print multiplication table for each number
        #if the integer is less than 0
            #inform user this program does not handle negative integers
        #ask the user if they want to play again
    #once the user answers no to playing again, exit the program


#prime the variable for the loop
play_again = "yes"

#begin main loop
while play_again!= "no":
    #obtain a number from the user
    integer =int(input("\nEnter an integer: "))
    print("")
    #test if integer is greater than 0
    if integer >= 0:
        #print multiplication  (1-12) for the number entered by user
        for num in range (1,13):
            print(f"{num} * {integer} = {num*integer}")
    #if integer is a negative number, tell the user
    else: print("This program does not handle negative numbers:")
    #ask the user to play again
    play_again = input("\nWould you like to run the program again? ")
print("\nExiting the program...")
    
