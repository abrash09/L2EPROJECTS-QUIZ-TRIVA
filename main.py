import random
from quiz_question import quiz
import sys
import select
import os

def run_quiz(question_list):
    shulffled_question = question_list.copy()
    random.shuffle(shulffled_question)
    quiz_questions = shulffled_question[:10]
    score = 0
    index = 0
    for index, q in enumerate(quiz_questions):
        print('='*45)
        print(f"Question {index + 1}: {q['question']}")
        print('='*45)
        for num, option in enumerate(q["options"]):
            print(f"{chr(97+num) }. {option}")
        while True:
            print("Enter your answer (a-d): ")
                    # This listens to the keyboard for 15 seconds
            ready, _, _ = select.select([sys.stdin], [], [], 15)
                
            if ready:
                user_answer = sys.stdin.readline().strip().lower()
            else:
                user_answer = "" # If they take too long, user_answer becomes empty
            if user_answer == "":
                print("Time up!")
                os.system('clear')
                break
            elif user_answer in ["a", "b", "c", "d"]:
                break
            else:
               print("Invalid input, please try again")  
        if user_answer != "":
            choice_index = ord(user_answer) - 97
            selected_option = q["options"][choice_index]
            if selected_option == q["answer"]:
                score += 1
                print("correct")
            else:
                print("wrong")
            os.system('clear')
    print(f"Your final score is:{score}/{len(quiz_questions)}")

def main():
    while True:
        print("Welcome to the Quiz")
        for subject in quiz.keys():
            print(subject)
        subject_choice = input("Type the subject you want to take: ").lower()
        run_quiz(quiz[subject_choice])
        play_again = input("Take another quiz? (y/n): ")
        if play_again == "y":
            continue
        else:
            break
if __name__ == "__main__":
    main()

