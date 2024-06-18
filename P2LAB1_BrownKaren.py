# Karen Brown
# June 18, 2024
# P2LAB1
# Brief Description: 
    #This program will obtain a radius from the user and return the diameter, circumference, and area of a circle.
#Detailed description: 
    #Gather input from the user and assign it to the variable radius, converting this to a float
    #import the math module
    #calculate diameter using the formula 2 * radius
    #calculate circumference using the formula 2 * pi * radius
    #calculate area by using the formula pi * radius**2
    #print the diameter to one decimal place
    #print the circumference to 2 decimal places
    #print the area to 3 decimal places 
     
radius = float(input("What is the radius of the circle? "))
import math
diameter = 2 * radius
circumference = 2 * math.pi * radius
area = math.pi * (radius**2)
print(f' \nThe diameter of the circle is {diameter:.1f}')
print(f' \nThe circumference of the circle is {circumference:.2f}')
print(f' \nThe area of the circle is {area:.3f}')
