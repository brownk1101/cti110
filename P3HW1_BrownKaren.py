#Karen Brown

#June 27, 2024

#P3HW1

# General description
    # This program takes a number grade , determines average and displays letter grade for average.

# Detailed description
    # Obtain input from user for 6 different module grades and assign them to variable mod_1 through mod_6
    # Convert these strings to a float
    # add these grades to the list "grades"
    # find the min of the list "grades"
    # find the max of the list "grades"
    # find the total sum of the list "grades"
    # find the average of the list "grades" by dividing sum by the length of the list
    # print the results to 1 decimal place, except average, which will print to 2 places
    # determine letter grade
        #if avg is greater or equal to 90
            #grade is A, print result
        #else if avg is greater or equal to 80
            #grade is B, print result
        #else if avg is greater or equal to 70
            #grade is C, print result
        #else if avg is greater or equal to 60
            #grade is D, print result
        #else
            #grade is F, print result
        


# Enter grades for six modules

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

# TO DO: determine lowest, highest , sum and average for grades

low = min(grades)
high = max(grades)
sum_of_grades = sum(grades)
avg = (sum(grades))/len(grades)


# print results
print("\n------------Results------------")
print(f"{'Lowest Grade:':<20} {low:.1f}")
print(f"{'Highest Grade:':<20} {high:.1f}")
print(f"{'Sum of Grades:':<20} {sum_of_grades:.1f}")
print(f"{'Average:':<20} {avg:.2f}")
print("----------------------------------------")


# determine letter grade for average

if avg >= 90:
    print('Your grade is: A')
elif avg >= 80:
    print('Your grade is: B')
elif avg >= 70:
    print('Your grade is: C')
elif avg >= 60:
    print('Your grade is: D')
else:
    print('Your grade is: F')







