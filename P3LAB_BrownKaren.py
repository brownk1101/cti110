 # Karen Brown
 # June 24, 2024
 # P3LAB
  
  #General description
      #This program will take a money value from the user and break down how many dollar bills, quarters, dimes, nickels, and pennies the user will need.
  #Detailed description
    ##Obtain from the user a monetary amount, convert it to a float, and assign to the variable total_money
    ##if total_money is any other amount print "No change"
    ##else
        ##Multiple total money by 100 to get a whole integer (this will be done for all other monetary values like 0.24, 0.10)
        ##Create variables for dollars, quarters, dimes, nickels, and pennies
        ##find the amount of dollars by floor dividng the total amount of money by 100 and convert it to an int. 
        ##subtract dollars* 100 to find the new total_money
        ##find the amount of quarters by floor dividng the total amount of money by 25 and convert it to an int. 
        ##subtract quarters * 25 to find the new total_money
        ##find the amount of dimes by floor divding the total amount of money by 10 and convert it to an int. 
        ##subtract dimes * 10 to find the new total_money
        ##find the amount of nickels by floor divding the total amount of money by 5 and convert it to an int. 
        ##subtract nickels * 5 to find the new total_money
        ##pennies equals the amount left over (total_money) converted to an int
        ##
        ##if dollars is greater than 1
            ##print the variable dollars with the description "Dollars"
        ##else if dollars is equal to 1,
            ##print the variable dollars with the description "Dollar"
    
        ##if quarters is greater than 1
            ##print the variable quarters with the description "Quarters"
        ##else if quarters is equal to 1
            ##print the variable quarter with the description "Quarter"
        
        ##if dimes is greater than 1
            ##print the variable dimes with the description "Dimes"
        ##else if dimes is equal to 1
            ##print the variable dime with the description "Dime"
        
        ##if nickels is greater than 1
            ##print the variable nickels with the description "Nickels"
        ##else if nicekls is equal to 1
            ##print the variable nickels with the description "Nickel"
        
        ##if pennies is greater than 1
            ##print the variable pennies with the description "Pennies"
        ##else if pennies is equal to 1
            ##print the variable pennies with the description "Penny"
        
          
      

#obtain input from user
total_money = float(input("Enter the amount of money as a float: $"))

if total_money == 0:
    print("No change")
else:
    #multiply by 100 to get a whole number
    total_money *= 100

    #assign variables
    #use floor division to find dollars, quarters, dimes, nickels, and pennies
        #multiply all change values by 100 (ex 0.25 *100) due to total_money originally being multiplied by 100
    dollars = int(total_money // 100)
    
    #subtract dollar amount from total_money to get new value
    total_money -= (dollars * 100)
    quarters = int(total_money // 25)
    total_money -= (quarters * 25)
    dimes = int(total_money // 10)
    total_money -= (dimes * 10)
    nickels = int(total_money // 5)
    total_money -= (nickels * 5)
    #Pennies is equal to what is left over
    pennies = int(total_money)

    #determine if the description needs to be singular or plural and print the amount
    if dollars > 1:
        print(f" {dollars} Dollars")
    elif dollars == 1:
        print(f" {dollers} Dollar")
        
    if quarters > 1:
        print(f" {quarters} Quarters")
    elif quarters == 1:
        print(f" {quarters} Quarter")

    if dimes > 1:
        print(f" {dimes} Dimes")
    elif dimes == 1:
        print(f" {dimes} Dime")

    if nickels > 1:
        print(f" {nickels} Nickels")
    elif nickels == 1:
        print(f" {nickels} Nickel")

    if pennies > 1:
        print(f" {pennies} Pennies")
    elif pennies == 1:
        print(f" {pennies} Penny")
    

    


    
    



