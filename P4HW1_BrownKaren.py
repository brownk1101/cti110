#Karen Brown

 #July 7, 2024

 #P4HW1

 #General Description
    #This assignment will get grade scores from a user displaying the lowest score, the scores after dropping the lowest grade, the average, and the student's letter grade.

 #Detailed description
    #create a list called scores
    #ask the user how many scores they wish to enter, assign this to variable num_of_scores
    #begin loop and have it run num_of_scores times
        #ask the user for the score
        #if entered score is between 0 and 100
            #append this score to the list scores
        #else
            #while entered score is less than 0 or more than 100
                #inform user score must be between 0 and 100
                #request corrected score
            #append entered score to the list scores
    #using the min function, find the lowest score in the list
    #remove the lowest score from the list
    #divide the sum of all the scores by the length of the list to find the average
    # determine letter grade
            #if avg is greater or equal to 90
                #grade is A
            #else if avg is greater or equal to 80
                #grade is B
            #else if avg is greater or equal to 70
                #grade is C
            #else if avg is greater or equal to 60
                #grade is D
            #else
                #grade is F
    #print the findings under the heading Results to 1 decimal place, except the average which will be 2 decimal places.
    #The descriptive data and the values should line up nicely by adjusting the width of the strings    

#create an empty list      
scores = []

#get number of scores from user
num_of_scores = int(input("How many scores do you wish to enter? "))
print("")

#begin loop
for score in range(1, num_of_scores +1):
    entered_score = float(input(f"Enter score #{score}: "))
    
    #test to see if score is between 0 and 100
    if 0 <= entered_score <= 100:
        #add it to the list
        scores.append(entered_score)
        
    #continue to ask the user for a valid score
    else:
        while entered_score < 0 or entered_score > 100:
            print("\nINVALID Score entered!!!!")
            print("Scor should be between 0 and 100")
            entered_score = int(input(f"Enter score #{score} again: "))
        scores.append(entered_score)
    
#Find the lowest score in the list
lowest_score = min(scores)

#Remove the lowest score
scores.remove(lowest_score)

#find the average
average_score = sum(scores)/len(scores)

#find the letter grade
if average_score >= 90:
    grade = "A"
elif average_score >= 80:
    grade = "B"
elif average_score >= 70:
    grade = "C"
elif average_score >= 60:
    grade = "D"
else:
    grade = "F"

#print results
print("\n------------Results------------")
print(f"{'Lowest Score':<14}: {lowest_score:.1f}")
print(f"{'Modified List':<14}: {scores}")
print(f"{'Scores Average':<14}: {average_score:.2f}")
print(f"{'Grade':<14}: {grade}")
print("---------------------------------")




    
    
