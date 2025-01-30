
score = 0

with open ('quizquestions.txt', 'r') as file:
    questions = file.readlines()

from random import *
random_line_number = randint(0, len(questions) - 1)
random_question = questions[random_line_number].strip()
print(f"Question: {random_question}")
 
 withopen("file.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

with open ('answers.txt' , 'r') as file:
    questions = file.readlines()
answer = input()
if answer in ('quizquestions.txt'):
    print("i think that's right")
else:
    print("wrong answer lol")
 