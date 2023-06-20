from paul_question_model import Question
from paul_data import question_data
from paul_data import science_data

from quiz_brain import QuizBrain
question_bank=[]

ask_user=input("Please select from a category: Type 'M' for Movie related questions Type 'S' for Science related: ")
if ask_user=="m".lower():
    for question in question_data:
    
        question_text=question["question"]
        answer_text=question["correct_answer"]
    
  
        new_question=Question(question_text,answer_text)
    
    
        question_bank.append(new_question)
else:
    for question in science_data:
    
        question_text=question["question"]
        answer_text=question["correct_answer"]
    
  
        new_question=Question(question_text,answer_text)
    
    
        question_bank.append(new_question)



quiz=QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()






