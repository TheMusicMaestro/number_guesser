# this is a number guesser game :)
# run this game in the command line using: .venv/bin/python3 main.py

import inquirer
from game import play_game
from stats import view_stats, reset_stats


def main():
    """Main function to display the menu and handle user choices."""

    while True:
        questions = [
            inquirer.List(
                "choice",
                message="What would you like to do?",
                choices=["Play Game", "View Stats", "Reset Stats", "Quit"],
            ),
        ]
        answers = inquirer.prompt(questions)

        if answers["choice"] == "Play Game":
            play_game()
        elif answers["choice"] == "View Stats":
            view_stats()
        elif answers["choice"] == "Reset Stats":
            reset_stats()
        elif answers["choice"] == "Quit":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
