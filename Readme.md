🧠 Python Multi-Subject Quiz App

A terminal-based quiz application built in pure Python. Test your knowledge in Math or English! Answer 10 random questions against a live ticking 2-minute timer.
✨ Features

    Multiple Subjects: Choose between different subjects (Math, English).
    Randomized Questions: Questions are shuffled every time you play, so you don't get the same order twice.
    10 Questions Per Round: A quick, 10-question test pulled from a larger pool of questions.
    Live Countdown Timer: You have 120 seconds to finish the quiz. Watch the clock tick down live while you think!
    Instant Feedback: The app tells you immediately if you were correct or wrong, and shows the right answer if you made a mistake.
    Input Validation: The app prevents crashes by trapping invalid inputs (like typing "z" instead of "a").

📁 Project Files

This project is split into two files to separate data from logic:

    main.py: The main application file. It contains the menu, the timer logic, and the scoring system.
    quiz_question.py: The data file. It holds all the questions, options, and answers organized by subject in a dictionary.

🚀 How to Run This Project (For Beginners)

Follow these simple steps to run the quiz on your computer:
Step 1: Install Python

If you don't have Python installed, download and install it from python.org. (This app works best on Linux, Mac, or Windows Subsystem for Linux because of the live timer feature).
Step 2: Download the Code

Download this repository to your computer (either by cloning it or downloading the ZIP file and extracting it).
Step 3: Open Your Terminal

Open your terminal (Command Prompt/PowerShell on Windows, or Terminal on Mac/Linux) and navigate to the folder where you saved the project. Example: cd Desktop/multichoice_quiz
Step 4: Run the Application

Type the following command and press Enter:

python3 main.py

(Note: On some Windows computers, you might need to type python main.py instead).
🎮 How to Play

1.  When the program starts, it will print a welcome message and list the available subjects.
2.  Type the name of the subject you want to take (e.g., math or english) and press Enter.
3.  You will be given 10 questions. 
4.  Each question has 4 options labeled a, b, c, and d.
5.  At the bottom of the screen, you will see a live countdown timer.
6.  Type the letter of your answer and press Enter.
7.  If you type a wrong letter, it will ask you to try again.
8.  If the timer hits 0, the quiz ends automatically!
9.  At the end of the quiz, your final score out of 10 will be displayed.
10. You will be asked if you want to take another quiz. Type y to play again, or n to exit.