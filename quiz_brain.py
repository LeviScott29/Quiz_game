class QuizBrain():
    def __init__(self, q_list):
        self.question_number = 0
        self.questions_list = q_list
        self.user_score = 0

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        while True:
            check = input(f"Q.{self.question_number}: {current_question.text} (True/False):")
            if check == "True" or check == "False" or check == "stop":
                break
            else:
                print(" pick 'True' or 'False'")
        if check == "stop":
            return check
        elif check == current_question.answer:
            print("you are correct")
            self.user_score +=1
            print("current score", self.user_score, "/", self.question_number)
        else:
            print("you are incorrect")
            print("current score", self.user_score, "/", self.question_number)
