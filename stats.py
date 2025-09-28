# manages game statistics

import os
import inquirer

def no_record():
    print("No record set yet.")
    
def no_games():
    print("No games played yet.")

def view_stats():
    """Displays the game statistics."""

    print("\n------ Game Statistics ------")

    # print record.txt
    try:
        with open("record.txt", "r") as f:
            lines = f.readlines()
            if len(lines) == 2:
                record_holder = lines[0].strip()
                record_lowest_guess = lines[1].strip()
                print(
                    f"Record Lowest Guess: {record_lowest_guess} — Held by {record_holder}"
                )
            else:
                no_record()
    except FileNotFoundError:
        no_record()

    # print history.txt
    try:
        with open("history.txt", "r") as f:
            history = [int(line.strip()) for line in f.readlines()]
            if history:
                num_games = len(history)
                average_guesses = sum(history) / num_games
                print(f"Total Number of Games Played: {num_games}")
                print(f"Average Number of Guesses per Game: {average_guesses:.2f}")
            else:
                no_games()
    except FileNotFoundError:
        no_games()
    
    print("-----------------------------\n")


def reset_stats():
    """Resets all game statistics."""

    confirm = inquirer.confirm(
        "Are you sure you want to reset all stats? This cannot be undone.",
        default=False,
    )

    if confirm:
        # remove record.txt
        try:
            os.remove("record.txt")
            print("Record file reset.")
        except FileNotFoundError:
            print("Record file already empty.")

        # remove history.txt
        try:
            os.remove("history.txt")
            print("History file reset.")
        except FileNotFoundError:
            print("History file already empty.")
        
        print()
            

    else:
        print("Stats reset cancelled.\n")
