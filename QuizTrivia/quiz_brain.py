
class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        userAnswer = input(f"Q.{self.question_number}: {current_question.question} (True/False): ")
        self.check_answer(userAnswer, current_question.answer)

    def in_quest(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, userAnswer, correct_answer):
        if userAnswer.lower() == correct_answer.lower():
            print("Thats Right!!!")
            self.score += 1
        else:
            print("You Wrong!")
            print(f"The correct answer is: {correct_answer}")
        print(f"Your Score : {self.score}/{len(self.question_list)}\n")