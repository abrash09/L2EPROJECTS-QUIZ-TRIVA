quiz = [
    { 
        "question": "what is 2 + 2?",
        "options":  ["3", "4", "5", "6"],
        "answer": "4"
    },
    { 
        "question": "what is capital of nigeria?",
        "options":  ["Lagos", "Kano", "Abuja", "Abia"],
        "answer": "Abuja"
    },   
    {
        "question": "The driver and principal______ here?",
        "options": ["are", "is", "has", "they are"],
        "answer": "is"
    }
]

def run_quiz(question_list):
    for q in question_list:
        print(q["question"])
        for num, option in enumerate(q["options"]):
            print(f"{num +1}. {option}")
        user_answer = input("Enter your answer (1-4):")
        print(user_answer)

def main():
    print("Welcome to the Quiz")
    run_quiz(quiz)

if __name__ == "__main__": 
    main()

