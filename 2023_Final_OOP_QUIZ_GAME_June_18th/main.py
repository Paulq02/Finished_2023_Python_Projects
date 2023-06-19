from question_model import Question
from data import question_data

from quiz_brain import QuizBrain
#Here we have an empty list to append the new question objects that will have 2 attributes (q_text and q_answer) from the Question class we created in the question_model module
question_bank=[]

#This for loop iterates in the question_data list which is a list of dictionaries that have 2 key/value pairs

#One value being a random question to ask the user, the other value being the correct answer if the question asked is true or false 
for question in question_data:
    #To get a hold of the values inside the dictionary we must provide the key, in this list all the question keys are named "text"
    
    #To get a hold of the values inside the dictionary we must provide the key, in this list all the correct answer keys are named "answer"

    #After getting a hold of each of these 2 values, we assigned 2 variables to hold their value

    #"question_text" will hold the question that will be displayed to the user and "answer_text" will hold the correct answer
    question_text=question["question"]
    answer_text=question["correct_answer"]
    
    #After assigning variables to these values we are going to format these questions from the question class in another module we've imported

    #The question class takes the variables that weve assigned from the for loop and assigns attribute names for the values
    
    #Each question from the list will have the attribute name "q_text" and each correct answer from the list will have the attribute name "q_list"

    #A new QUESTION object will be created with every new interation from the for loop
    new_question=Question(question_text,answer_text)
    
    #After the for loop is finished and all the questions and answers have been formatted correctly we now append each newly formatted Question object to the empty list called "question_bank"
    question_bank.append(new_question)


quiz=QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()


