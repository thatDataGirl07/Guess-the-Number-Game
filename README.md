'Guess the Number' Game Variations Repository

This repository contains different variations of the classic "Guess the Number" game.
Currently, it features a robust game mode where:
1. The Computer guesses the number you're thinking of, and
2. The player guesses the number the computer's thinking of.

Game Mode 1: The Computer Guesses Your Secret Number
File Name: computer_guesses_number.py

Description: In this game mode, you think of a secret whole number, and the computer tries to guess it.
   It uses Binary Search to efficiently narrow down the search space with each iteration, leading to a quick and strategic guessing process.
   The computer dynamically generates a new, random range for the player to choose from, for each game round, ensuring the game stays lively.
   The game also catches inconsistent feedback from the player's input.
How to Play (quite easy):
    a.  The computer picks a random range (e.g., "Think of a number between 50 and 300").
    b.  You silently pick your secret number within that range.
    c.  When the computer makes a guess, you provide feedback:
        'H' (or 'h') for 'Too High'.
        'L' (or 'l') for 'Too Low'.
        'C' (or 'c') for 'Correct'.
    d.  See if the computer can guess your number before it runs out of attempts.

Game Mode 2: The Player Guesses the Computer's Secret Number
File Name: user_guesses_number.py

Description:  This is the classic "Guess the Number" game where the computer thinks of a secret number, and the player tries to guess it. The computer goes on to provide feedbacks (too high, too low, or correct), as the player provides guesses.


How to Run the Game

1.  Prerequisites: Make sure Python is installed on your system.
2.  You can clone the repository to your local machine OR download the repository as a ZIP file and then extract it.
3.  Run the Game:
    a. Open your terminal or Command Prompt.
    b. Navigate into 'YourRepoName' directory (if you haven't already with 'cd').
    c. To play, run:
   
       'python computer_guesses_number.py'

---

Language: Python

---
Contributions are Welcome!🤝 Feel free to clone this repository, and add to the code. 

