# used to boot up the game

import inquirer #allows for user input multi-selec
from game import play_game
from stats import view_stats, reset_stats


def main():
    """Main function to display the menu and handle user choices."""

    while True:
        questions = [
            inquirer.List(
                "choice",
                message="Select an option:",
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
            print("Goodbye!\n")
            break


if __name__ == "__main__":
    main()
