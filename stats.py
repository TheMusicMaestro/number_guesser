import os
import inquirer


def view_stats():
    """Displays the game statistics."""

    print("\n--- Game Statistics ---")

    try:
        with open("record.txt", "r") as f:
            record = f.read()
            print(f"Record Lowest Guess: {record}")
    except FileNotFoundError:
        print("No record set yet.")

    try:
        with open("history.txt", "r") as f:
            history = [int(line.strip()) for line in f.readlines()]
            if history:
                num_games = len(history)
                average_guesses = sum(history) / num_games
                print(f"Total Number of Games Played: {num_games}")
                print(f"Average Number of Guesses per Game: {average_guesses:.2f}")
            else:
                print("No games played yet.")
    except FileNotFoundError:
        print("No games played yet.")
    print("-----------------------\n")


def reset_stats():
    """Resets all game statistics."""

    confirm = inquirer.confirm(
        "Are you sure you want to reset all stats? This cannot be undone.",
        default=False,
    )
    if confirm:
        try:
            os.remove("record.txt")
            print("Record file reset.")
        except FileNotFoundError:
            print("Record file already empty.")
        try:
            os.remove("history.txt")
            print("History file reset.")
        except FileNotFoundError:
            print("History file already empty.")
        print("Stats have been reset.\n")
    else:
        print("Stats reset cancelled.\n")
