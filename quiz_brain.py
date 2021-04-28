class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        user_answer = input(f"N.{self.question_number + 1} | {current_question.text} | True or False? ")
        self.question_number += 1
        self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self):
        if self.question_number < len(self.question_list) and not self.question_number == -1:
            return True
        else:
            return False

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print(f"You guessed it right!")
        else:
            print(f"You guessed it wrong... The correct answer is {correct_answer}.")
            self.question_number = -1
        print("")
