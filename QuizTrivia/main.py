from data import easy, hard
from question_model import Question
from quiz_brain import QuizBrain
import art

print(art.logo)

difficult = input(" -Easy \n -Hard \nChoose the difficult: ").lower()
question_bank_easy = []
question_bank_hard = []

if difficult == "easy":
    for data in easy:
        newquestion_bank = Question(data["question"], data["correct_answer"])
        question_bank_easy.append(newquestion_bank)
    quiz = QuizBrain(question_bank_easy)
else:
    for data in hard:
        newquestion_bank = Question(data["question"], data["correct_answer"])
        question_bank_hard.append(newquestion_bank)
    quiz = QuizBrain(question_bank_hard)

while quiz.in_quest():
    quiz.next_question()

print(art.win)
print("Congrats!!! For Completing this Question")
print(f"Your final score is {quiz.score}")
