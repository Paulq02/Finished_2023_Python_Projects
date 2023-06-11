class QuizBrain:
    def __init__(self,q_list) -> None:
        self.q_list=q_list
        self.question_number=0

    def next_question(self):
        current_question=self.q_list[self.question_number]
        input(f"Q.{self.question_number}:{current_question.text} (True or False?): ")


        
        


    
        



        

    


        
        

        

