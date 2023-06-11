class QuizBrain:
    def __init__(self,q_list) -> None:
        self.question_number=0
        self.q_list=q_list


    def still_has_questions(self):
        if curre

    def next_question(self):
        current_question=self.q_list[self.question_number]
        self.question_number+=1
        new_question=input(f"Q.{self.question_number}: {current_question.q_text}(True of False?): ")

        
    
        



        

    


        
        

        

