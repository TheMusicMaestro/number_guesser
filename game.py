import random


def get_integer_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a whole number.")


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

    random_number = random.randint(1, 100)
    num_guesses = 0
    invalid_guesses = 0

    guess = get_integer_input("Guess a number between 1 and 100: ")

    while True:
        if guess == random_number:
            print(f"\nThat's right, the number is {random_number}!")
            print(f"You guessed the number in {num_guesses} tries.")

            try:
                with open("history.txt", "r") as f:
                    history = [int(line.strip()) for line in f.readlines()]
                    if history:
                        average_guesses = sum(history) / len(history)
                        print(f"Historical average: {average_guesses:.2f}.")
            except FileNotFoundError:
                pass

            print(f"The current record lowest guess is {record_lowest_guess}.")

            if num_guesses < record_lowest_guess:
                record_lowest_guess = num_guesses
                with open("record.txt", "w") as f:
                    f.write(str(record_lowest_guess))
                print("Congratulations! You broke the record and now hold the title!")

            with open("history.txt", "a") as f:
                f.write(str(num_guesses) + "\n")

            print("Thanks for playing!\n")
            break

        elif guess > 100 or guess < 1:
            if invalid_guesses < 1:
                print("Hmm... please ready the instructions and try again.")
                invalid_guesses += 1
            else:
                print("\nPlease learn to read and try again next time.")
                print("Game over!\n")
                break

        elif guess < random_number:
            print("Too low!")

        else:
            print("Too high!")

        guess = get_integer_input("Guess again: ")
        num_guesses += 1
