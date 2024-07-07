# Karen Brown   

# July 7, 2024

# P4HW2

# General Description
    # This program will calculate gross pay for multiple employees. It will also
    # calculate total amount paid for overtime, regular pay, and total amount for
    # all employees

# Detailed description
    #prime the following variables that will be used in the program
        #num_employees 
        #total_all_hours
        #total_ot_paid
        #total_gross_paid 
        #overtime_hours
        #overtime_pay
        #regular_pay
        #total_reg_hours_paid        
    #  obtain employees name from user, assign it to variable employee_name
    # begin the main loop if employee name is not "Done"
        # obtain number of hours worked from user, assign it to the variable total_hours
        # obtain employee's pay rate from the user, assign it to the variable pay_rate
        # if total hours is more than 40 hours
            # calculate overtime hours by subtracting 40 from total hours
            # calculate regular pay rate by multiplying pay rate by 40
            # calculate overtime pay by multiplying overtime hours by pay rate by 1.5
            # calculate gross pay by adding regular pay and overtime pay
            # add overtime pay to total ot paid
        # else no over time worked
            # gross pay is equal to total hours times pay rate
            # regular pay is the same as gross pay

            # get the totals for all employees
            # add 1 to num of employees
            # add total hours to total all hours
            # add gross pay to total gross pay
            # add regular pay to total reg hours paid
        # print the following
            # Employee's name
            # the following headings and their corresponding values in columns underneath 
                # Hours Worked
                # Pay Rate
                # Overtime
                # Overtime Pay
                # Regular Pay
                # Gross Pay
        # obtain the next employee from the user
    # when user types "Done"
    # print total number of employees
    # print total amount paid for overtime
    # print total amount paid for regular hours
    # print total gross amount paid 



# prime variables
employee = ""
num_employees = 0
total_all_hours = 0
total_ot_paid = 0
total_gross_paid = 0
overtime_hours = 0
overtime_pay = 0
regular_pay = 0
total_reg_hours_paid = 0

# get employee name from user
employee_name = input(f"Enter employee's name of \"Done\" to terminate: ")

#begin main loop
while employee_name != "Done":
    #Obtain name, hours, and pay rate from user
    total_hours = float(input("Enter number of hours worked: "))
    pay_rate = float(input("Enter employee's pay rate: "))

    #determine if overtime hours were worked
    if total_hours > 40:
        overtime_hours = total_hours - 40
        #calculate regular pay
        regular_pay = pay_rate * 40
        #calculate overtime pay
        overtime_pay = overtime_hours * (pay_rate * 1.5)
        #calculate gross_pay
        gross_pay = regular_pay + overtime_pay
        total_ot_paid += overtime_pay
    else:
        gross_pay = total_hours * pay_rate
        regular_pay = gross_pay

    #add to the totals for all employees
    num_employees += 1
    total_all_hours += total_hours
    total_gross_paid += gross_pay
    total_reg_hours_paid += regular_pay
    


    print(f"\n{'Employee Name:':<17} {employee_name}")
    print(f"\n{'Hours Worked':<15}{'Pay Rate':<12}{'Overtime':<12}{'OverTime Pay':<20}{'RegHour Pay':<20}{'Gross Pay':<19}")
    print("----------------------------------------------------------------------------------------------")        
    print(f"{total_hours:<15}{pay_rate:<12}{overtime_hours:<12}${overtime_pay:<20.2f}${regular_pay:<20.2f}${gross_pay:<19.2f}") 

    employee_name = input("Enter employee's name of \"Done\" to terminate: ")
    
print(f"\nTotal number of employees entered: {num_employees}")
print(f"Total amount paid for overtime: ${total_ot_paid:.2f}")
print(f"Total amount paid for regular hours: ${total_reg_hours_paid:.2f}")
print(f"Total amount paid in gross: ${total_gross_paid:.2f}") 
