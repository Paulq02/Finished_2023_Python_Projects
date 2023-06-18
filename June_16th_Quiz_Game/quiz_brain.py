class QuizBrain:
    def __init__(self,q_list) -> None:
        self.q_list=q_list
        self.question_number=0
        self.score=0
    
    def still_has_questions(self):
        if self.question_number<len(self.q_list):
            return True
        else:
            return False


    def next_question(self):
        current_question=self.q_list[self.question_number]
        self.question_number+=1
        user_answer=input(f"Q.{self.question_number}: {current_question.q_text}. (True or False):  ")
        self.check_answer(user_answer,current_question.q_answer)

    def check_answer(self,user_input,correct_answer):
        if user_input.lower()==correct_answer.lower():
            print("Correct!")
            self.score+=1
        else:
            print("Sorry that was incorrect")
        print(f"The answer is: {correct_answer}")
        print(f"Your current score is {self.score}/{self.question_number}")



        
        
                                     
        