# Karen Brown

# June 27, 2024

# P3HW2

# General Description
    # This program will take an employees hours and calculate their gross pay based off of their regular and overtime hours

# Detailed Description
    # obtain employees name from user, assign it to variable employee_name
    # obtain number of hours worked from user, assign it to the variable total_hours
    # obtain employee's pay rate from the user, assign it to the variable pay_rate
    # if total hours is more than 40 hours
        # calculate overtime hours by subtracting 40 from total hours
        # calculate regular pay rate by multiplying pay rate by 40
        # calculate overtime pay by multiplying overtime hours by pay rate by 1.5
        # calculate gross pay by adding regular pay and overtime pay

    # else
        # calculate gross pay by multiplying total hours by pay rate
        # regular pay is the same as gross pay
        # overtime hours and pay is 0
    #print the following
        #Employee's name
        #the following headings and their corresponding values in columns underneath 
            #Hours Worked
            #Pay Rate
            #Overtime
            #Overtime Pay
            #Regular Pay
            #Gross Pay


#Obtain name, hours, and pay rate from user

employee_name = input("Enter employee's name: ")
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
else:
    gross_pay = total_hours * pay_rate
    regular_pay = gross_pay
    overtime_hours = 0
    overtime_pay = 0

print("-------------------------------------")
print(f"{'Employee Name:':<17} {employee_name}")
print(f"\n{'Hours Worked':<15}{'Pay Rate':<12}{'Overtime':<12}{'OverTime Pay':<20}{'RegHour Pay':<20}{'Gross Pay':<19}")
print("----------------------------------------------------------------------------------------------")        
print(f"{total_hours:<15}{pay_rate:<12}{overtime_hours:<12}${overtime_pay:<20.2f}${regular_pay:<20.2f}${gross_pay:<19.2f}") 
