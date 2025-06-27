import random
import os
import math


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def guessing_game():
    """ Implements a guessing game where the computer guesses a secret number chosen by the player."""
    play_again = "y"

    print("Hey, welcome to Guess the Number! Computer here, by the way.")
    #print("I'll set a new range for you to think of a number within for each round.")

    while play_again.lower() == "y":
        #clear_screen()  # Clears the screen at the start of every new game round.

        overall_min_possible_val = 1
        overall_max_possible_val = 1000
        min_range_size = 50  # Ensures the randomly chosen range is at least 50 numbers wide, to avoid ranges like 5,7.

        start_point = random.randint(overall_min_possible_val, overall_max_possible_val - min_range_size)

        end_point = random.randint(start_point + min_range_size, overall_max_possible_val)

        low = start_point
        high = end_point
        attempts = 0
        guessed_correctly = False
        inconsistent_feedback_detected = False

        print(f"\nFor this round, think of a number between {low} and {high}, and I'll try to guess it.")
        print("\nGive me hints: H for 'High', L for 'Low', or C for 'Correct'!")
        input("Press Enter when you're ready to start...")

        max_attempts_per_round = math.ceil(math.log2(high - low + 1)) #To get the optimal number of max attempts.

        # Inner game loop for each game round.
        while attempts < max_attempts_per_round:
            attempts += 1


            # If the range has collapsed to a single number, then that'd be the guess.
            if low == high:
                guess = low
            else:
                guess = (low + high) // 2  # Guess utilizes binary search to identify the user's secret number.

            # Lower bound being greater than the higher bound; inconsistency detected.
            if low > high:
                inconsistent_feedback_detected = True
                print("Uhmm, your feedbacks are inconsistent, making it impossible to guess.")
                break  # Exits the inner loop immediately.

            print(f"My guess is: {guess}")
            feedback = input("Is my guess 'High' (H), 'Low (L), or 'Correct' (C)? ").lower().strip()

            if feedback == "h":
                high = guess - 1
            elif feedback == "l":
                low = guess + 1
            elif feedback == "c":
                print(f"Yay, the computer has guessed your number, {guess} correctly, in {attempts} attempt(s)!")
                guessed_correctly = True  # The flag gets updated, because the number has been guessed correctly.
                break  # Gets out of the inner loop immediately.

            else:
                print("Invalid input. Please, enter 'H' for High, 'L' for Low, or 'C' for Correct.")
                attempts -= 1  # Invalid input doesn't get counted as a successful attempt.

        # Outside the inner game loop.
        if guessed_correctly:
            # Message already printed inside the inner game loop.
            pass
        elif inconsistent_feedback_detected:
            print("\nOuch, I couldn't guess your number because I received inconsistent feedback.")
            print("Please, double-check your number and the hints you give next time.")
        else:
            print(f"\nI'm sorry, I couldn't guess your number within {max_attempts_per_round} attempts.")
            print("Thanks for playing, though!")

        play_again = input("\nDo you want to play again? (Y/N): ").lower().strip()

        # Input validation for play_again.
        while play_again not in ["y", "n"]:
            play_again = input("Invalid input. Please, enter 'Y' for Yes, or 'N' for No: ").lower().strip()

        if play_again == "y":
            clear_screen()  # Clears the screen at the start of every new game round.
            print("\nWelcome back for another round!")
        else:
            print("Thanks for playing with me! Goodbye!")


guessing_game()
