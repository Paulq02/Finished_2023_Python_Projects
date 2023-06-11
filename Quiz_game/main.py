from quiz_brain import QuizBrain

from question_model import Question



from data import question_data

 

question_bank=[]

for question in question_data:
    text_question=question["text"]
    text_answer=question["answer"]
    new_question=Question(text_question,text_answer)
    question_bank.append(new_question)

quiz=QuizBrain(question_bank)

while 
quiz.next_question()











