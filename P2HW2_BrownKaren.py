#Karen Brown

 #Jue 22, 2024

 #P2HW2

 #General Description
    #Create a list for the user to store grades in. Then find the lowest, highest, total, and average of the grades.

 #Detailed description
    #Create an empty list called module_grades
    #Ask the user to enter grades for 6 different modules
    #Assign each of these inputs to the variable module1_grade, module2_grade, module3_grade, module4_grade, module5_grade, module6_grade
    #After each user input, append the variable to the list called module_grades
    #using the min function, find the lowest grade in the list
    #using the max function, find the highest grade in the list
    #using the sum function, find the sum of all the grades
    #divide the sum by the length of the list to find the average
    #print the findings under the heading Results to 1 decimal place, except the average which will be 2 decimal places.
    #The descriptive data and the values should line up nicely by adjusting the width of the strings
#create an empty list
module_grades = []

#receive input for modules 1 though 6, convert it into float, and store it in variables
#add each value to the list called module_grades
module1_grade = float(input("Enter a grade for Module 1: "))
module_grades.append(module1_grade)
module2_grade = float(input("Enter a grade for Module 2: "))
module_grades.append(module2_grade)
module3_grade = float(input("Enter a grade for Module 3: "))
module_grades.append(module3_grade)
module4_grade = float(input("Enter a grade for Module 4: "))
module_grades.append(module4_grade)
module5_grade = float(input("Enter a grade for Module 5: "))
module_grades.append(module5_grade)
module6_grade = float(input("Enter a grade for Module 6: "))
module_grades.append(module6_grade)

#Find the lowest grade in the list
lowest_grade = min(module_grades)

#Find the highest grade in the list
highest_grade = max(module_grades)

#Find the sum of all the grades in the list
sum_of_grades = sum(module_grades)

#Find the average of all the grades
average_grade = sum(module_grades)/len(module_grades)

#Print the finidings above. All will be to 1 decimal place, except average, which will be to two decimal places
#Set the string width to 20 places
print("\n------------Results------------")
print(f"{'Lowest Grade:':<20} {lowest_grade:.1f}")
print(f"{'Highest Grade:':<20} {highest_grade:.1f}")
print(f"{'Sum of Grades:':<20} {sum_of_grades:.1f}")
print(f"{'Average:':<20} {average_grade:.2f}")
print("----------------------------------------")


