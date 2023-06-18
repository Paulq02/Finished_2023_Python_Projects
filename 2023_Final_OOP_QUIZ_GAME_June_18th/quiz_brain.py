class QuizBrain:

    #This init function takes the "question_bank" list as input from the main.py module

    #We also made 2 default values/attributes - "question_number" which represents the current question number you are on 

    #The other default attribute is the score, which we use to keep track of how many questions the user gets correct 

    def __init__(self,question_list) -> None:
        self.question_list=question_list
        self.question_number=0
        self.score=0
         

    #This method "next_question" get a hold of the current list iteration of the for loop (which by default starts at 0 )

    def next_question(self):
        #The "question_bank" holds all the formatted questions- so for instance, "self.question_list" is the "question_bank"
        #The "self.question_number" is the index position - So self.question_list[self.question_number] is equal to question_bank[0]
        #Each new question object would look like this - question_bank[0]=new_question(q_text,q_answer) this would be the first question then go to question 2 and so on

        current_question=self.question_list[self.question_number]
        #Since we want our current question to be displayed starting with 1 we need to add 1 to the "self.question_number" attribute
        #The "self.question_number" by default starts at 0 since it's the index postion and list index postions start at 0
        self.question_number+=1

        #To display the current question and get user input to make a guess we use the input function as an f string 
        #We also insert the "self.question_number" attribute along with the "self.q_text" atrribute to display the question number and the question that is being asked to the user
        user_answer=input(f"Q.{self.question_number}: {current_question.q_text} (True or False)?: ")
        self.check_answer(user_answer,current_question.q_answer)


    def still_has_questions(self):
        """
        checks if the current question number is less than how many questions are in the list
        returns a value of True if there are still more questions in the list, returns false if not
        """
        return self.question_number < len(self.question_list)
    
    def check_answer(self,user_input,correct_answer_input):
        """
        Checks the users guess to see if it matches the correct answer,
        prints "correct" if guess is right then adds 1 to the score attribute, prints "incorrect" if user is wrong,
        Also prints the correct answer to the user regardless if they are right or wrong, prints correct guesses out of how many questions you've seen


        """
        if user_input.lower()==correct_answer_input.lower():
            print("Correct!")
            self.score+=1
        else:
            print("Sorry that was incorrect")
        print(f"The answer is {correct_answer_input} ")
        print(f"Your score is {self.score}/{self.question_number}")
        print("\n")

    

