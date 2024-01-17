from question_model import Question
from data import general_q, music_q, computers_q
from quiz_brain import QuizBrain
category_options = { "computers": computers_q,
                     "general": general_q,
                     "music": music_q}

while True:
    question_bank = []
    while True:

        option = input(" do you want questions on 'general', 'computers', or 'music'?: ")
        if option == "general" or option =="computers" or option =="music":
            break
        else:
            print("pick a correct category")

    cat_select = category_options.get(option)
    while True:
        difficulty = input(" what difficulty 'easy', or 'medium': ")
        if difficulty == "easy" or difficulty == "medium":
            break
        else:
            print("pick a difficulty")
    for question in cat_select:
        if difficulty == "medium":
            if question.get("difficulty") == difficulty:
                question_text = question["question"]
                question_answer = question["correct_answer"]
                new_question = Question(question_text, question_answer)
                question_bank.append(new_question)
        if difficulty == "easy":
            if question.get("difficulty") == difficulty:
                question_text = question["question"]
                question_answer = question["correct_answer"]
                new_question = Question(question_text, question_answer)
                question_bank.append(new_question)

    quiz = QuizBrain(question_bank)
    answer = ""
    while quiz.still_has_questions():
        answer = quiz.next_question()
        if answer == "stop":
            break
    print("end of quiz")
    print("your final score is: ", quiz.user_score,"/", quiz.question_number)
    while True:
        play_again = input("do you want to play again?: ")
        if play_again == "yes":
            break
        if play_again == "no":
            break
    if play_again == "no":
        break
