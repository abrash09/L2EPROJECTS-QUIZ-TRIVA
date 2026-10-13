import random
from quiz_question import quiz
import time
import sys
import select


def run_quiz(question_list):
    time_limit = 120
    start_time = time.time()
    shulffled_question = question_list.copy()
    random.shuffle(shulffled_question)
    quiz_questions = shulffled_question[:10]
    score = 0
    index = 0
    print(f"\nGet ready! You have {time_limit} seconds to answer {len(quiz_questions)} questions.\n")

    for index, q in enumerate(quiz_questions):
        print('='*45)
        print(f"Question {index + 1} of {len(quiz_questions)}")
        print('='*45)
        print(f"{q['question']}")
        for num, option in enumerate(q["options"]):
            print(f"{chr(97+num) }. {option}")

        user_answer = ""
        print(f"⏳ Time remaining: 120 sec | Enter your answer (a-d): ", end="", flush=True)
        
        while True:
            elapsed_time = time.time() - start_time
            if elapsed_time > time_limit:
                print("\n[⏰ Time is up for this quiz!") 
                break 
            ready, _, _ = select.select([sys.stdin], [], [], 1.0)

            if ready:
                user_answer = sys.stdin.readline().strip().lower()
                if user_answer in ["a", "b", "c", "d"]:
                    print("\033[, end=")
                    break
                else:
                    print("\033[KInvalid input. Try again: ", end="", flush=True)
            else:
                time_left = int(time_limit - elapsed_time)
                print(f"\r⏳ Time remaining: {time_left:02d} sec | Enter your answer (a-d): ", end="", flush=True)

        if elapsed_time <= time_limit and user_answer in ["a", "b", "c", "d"]:
            choice_index = ord(user_answer) - 97
            selected_option = q["options"][choice_index]
            if selected_option == q["answer"]:
                score += 1
                print("correct\n")
            else:
                print("wrong\n")
    print(f"Your final score is: {score}/{len(quiz_questions)}")

def main():
    while True:
        print("Welcome to the Quiz\n")
        print(f"Get ready! You have 120 seconds to answer 10 questions.\n")
        for subject in quiz.keys():
            print(subject)
        subject_choice = input("Type the subject you want to take: \n").lower()
        run_quiz(quiz[subject_choice])
        play_again = input("Take another quiz? (y/n): ")
        if play_again == "y":
            continue
        else:
            break
if __name__ == "__main__":
    main()

