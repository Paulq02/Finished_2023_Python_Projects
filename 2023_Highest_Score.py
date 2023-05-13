# Angelas code is a little confusing 

# This program outputs the Highest score from what you input

#Student_scores takes multiple inputs with the .split method

#Then is converted to an integer





#Angelas code
# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)




#I made a for loop to iterate in the list input (student_scores)

#The variable "score" will equal every input one at a time

#"score" will compare itself to highest_score and if it's larger than highestr score it will reset the highest score to 0 then add the current iteration as the highest score

# If I entered 101, 102, 103 :"score" will equal 101 first compare it to highest_score which is 0 then reset the score to 0 again and add 101 as the highest_score

#Then the following loop score will equal 102, compares 102 to 101. 102 is larger so it will reset the highest score to 0 and add 102 as the highest score
#MY CODE
# 🚨 Don't change the code above 👆
highest_score=0
for score in student_scores:
  if score>highest_score:
    highest_score=0
    highest_score+=score

print(highest_score)