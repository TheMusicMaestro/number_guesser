# runs the game itself

import random


def is_int(value: str) -> bool:
    """Return True if value can be safely converted to an int, otherwise False."""
    try:
        int(value)
        return True
    except ValueError:
        return False


def last_chance():
    print(
        "Make sure your guess is an integer between 1 and 100... this is your last chance!\n"
    )


def play_game():
    """The main game logic."""
    try:
        with open("record.txt", "r") as f:
            read_value = float(f.read())
            if read_value == float("inf"):
                record_lowest_guess = float("inf")
            else:
                record_lowest_guess = int(read_value)
    except (FileNotFoundError, ValueError):
        record_lowest_guess = float("inf")

    # variable assignments
    random_number = random.randint(1, 100)
    num_guesses = 0
    invalid_guesses = 0

    while True:
        # user input
        guess_input = input("Guess a number between 1 and 100: ")

        # test if guess is an integer / illegal guess
        if not is_int(guess_input):
            if invalid_guesses == 0:
                last_chance()
                invalid_guesses += 1
            else:
                print("\nGAME OVER!\n")
                break
            continue

        guess = int(guess_input)
        num_guesses += 1

        # out of bounds guess
        if guess < 1 or guess > 100:
            if invalid_guesses == 0:
                last_chance()
                invalid_guesses += 1
            else:
                print("\nGAME OVER!\n")
                break

        # legal guess
        elif guess < random_number:
            print("Too low!")
        elif guess > random_number:
            print("Too high!")

        # correct guess
        elif guess == random_number:
            # print winner message
            print("\nWINNER!")
            print(f"You guessed the number in {num_guesses} tries.")

            # print historical average
            try:
                with open("history.txt", "r") as f:
                    history = [int(line.strip()) for line in f.readlines()]
                    if history:
                        average_guesses = sum(history) / len(history)
                        print(f"The historical average is {average_guesses:.2f} tries.")
            except FileNotFoundError:
                pass

            # print current record
            if record_lowest_guess != float("inf"):
                print(f"The current record lowest guess is {record_lowest_guess}.")
            else:
                print("You are the first to play!")

            # print new record
            if num_guesses < record_lowest_guess:
                record_lowest_guess = num_guesses
                with open("record.txt", "w") as f:
                    f.write(str(record_lowest_guess))
                print("NEW RECORD!")
                print("Congratulations, you now hold the top spot!")

            with open("history.txt", "a") as f:
                f.write(str(num_guesses) + "\n")

            print("Thanks for playing!\n")
            break

        else:
            raise Exception("You broke the game!")
            break
