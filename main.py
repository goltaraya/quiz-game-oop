# Quiz Game with OOP
# Author >>> Yago Goltara

from question_model import Question  # From < question_model.py > import < class Question >
from data import question_data       # From < data.py > import < list question_data >
from quiz_brain import QuizBrain     # From < quiz_brain.py > import < class QuizBrain>
from logo import logo

question_bank = []  # Create a list to store the questions

for position in range(len(question_data)):  # For-loop to manipulate the list and append each time a new question
    new_question = Question(question_data[position]["text"], question_data[position]["answer"])
    question_bank.append(new_question)

quiz_game = QuizBrain(question_bank)    # Create the quiz object

print(logo)
name = input("Hey! Welcome to a general knowledge quiz. First, write your name: ")  # Get the user's name
input(f"Alright, {name}! Let's start our game! Press 'ENTER' to start.\n\n")        # Ordinary greetings

while quiz_game.still_has_questions():      # While-loop which starts the quiz game
    quiz_game.next_question()

    if quiz_game.score == len(quiz_game.question_list):     # If the user answers everything correctly then:
        print("You've completed the quiz! Congratulations!")

print(f"Your final score was: {quiz_game.score} /", len(quiz_game.question_list))   # Display the final score
input()     # Stop
