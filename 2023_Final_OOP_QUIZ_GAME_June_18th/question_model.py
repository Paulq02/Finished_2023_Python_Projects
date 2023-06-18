class Question:

    #The question class initializes attribute names for the values "question_text" and "question_answer" 

    #"question_text" and "question_answer" are the variables storing the values of the question and answer we've collected from the "data list"

    def __init__(self,q_text,q_answer) -> None:
        self.q_text=q_text
        self.q_answer=q_answer

    
