import os
import random


def reset_game():
    consecutive_out_of_range = 0
    consecutive_high_guess = 0
    consecutive_low_guess = 0
    user_input = None
    attempt = 0
    print("\n" * 2)


def guess(x):
    play_again = "y"
    while play_again.lower() == "y":

        consecutive_out_of_range = 0
        consecutive_high_guess = 0
        consecutive_low_guess = 0
        user_input = 0
        attempt = 0

        random_number = random.randint(1, x)
        number = 0
        while number != random_number and attempt < 5:
            if user_input == 0:
                while True:
                    try:
                        name_of_user = (input("What should we call you? "))
                        print(f"Hi, {name_of_user}. Hello and Welcome to Guess the Number! You have only 5 attempts! "
                              f"Let's go!")
                        number = int(input(f"I have a number on my mind. It's between 1 and {x}... \nCan you guess? "))
                        break
                    except ValueError:
                        print("Please, enter a valid number! ")

            elif user_input == 1:
                while True:
                    try:
                        number = int(input("Try again! "))
                        break
                    except ValueError:
                        print("Please, enter a valid number!")

            elif user_input >= 2 and attempt < 5:
                while True:
                    try:
                        number = int(input("You're losing money! "))
                        break
                    except ValueError:
                        print("Please, enter a valid number! ")
            user_input += 1
            attempt += 1

            if number > x:
                if consecutive_out_of_range == 0:
                    print("Out of range...", end=" ")
                elif consecutive_out_of_range == 1:
                    print("Still out of range...", end=" ")
                elif consecutive_out_of_range == 2:
                    print("Are you sure about your range?...", end=" ")
                elif consecutive_out_of_range >= 3:
                    print("Ranger Joe, you're out of range!", end=" ")
                consecutive_out_of_range += 1

            if number < random_number and type(number) == int:
                if consecutive_low_guess == 0:
                    print("Too low!", end=" ")
                elif consecutive_low_guess == 1:
                    print("Still too low!", end=" ")
                elif consecutive_low_guess >= 2:
                    print("You're still stuck down, aren't you?...", end=" ")
                consecutive_low_guess += 1

            if random_number < number <= x:
                if consecutive_high_guess == 0:
                    print("Too high!", end=" ")
                elif consecutive_high_guess == 1:
                    print("High up in the clouds, baby!...", end=" ")
                elif consecutive_high_guess >= 2:
                    print("Hello! You're still way up...", end=" ")
                consecutive_high_guess += 1

        if attempt > 4 and number != random_number:
            print(f"\n" * 2, f"But, Oops! You're out of guesses! The number actually is {random_number}. Nice try, though.")

        if number == random_number:
            print(f"\nYay! You finally arrived here. The number is indeed {random_number}.")

        play_again = input("Play again? Y/N ").lower()
        if play_again == "n":
            print("Thanks for playing!")
        elif play_again == "y":
            reset_game()


guess(100)        # 100 is the guess range.


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


clear_console()
