#The way Angela wrote this intital code is SUPER CONFUSING

#Bascially she wants you to enter a bunch of heights in CENTEMETERS

#Then have a for loop add them all together then divide them by how many imputs there were

#The .split() Method allows for multiple inputs

#You created 2 varibles with a value of 0 to store data

#Then you wrote your for loop iterating in the list "student_heights"

#"height" will be equal to every interation of your input

#So we have "height" add to total for every iteration

#Then for every loop we add 1 to the "person" variable to replicate the len function

#We get a number for the "person" variable of how many entries we have and use that to divide by all the entries added up

# We then use the round function to round it to the nearest whole number





# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
total=0
person=0
for height in student_heights:
  total+=height
  person+=1
final=round(total/person)
print(final)