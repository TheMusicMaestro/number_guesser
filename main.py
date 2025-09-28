# used to boot up the game

# this tool allows for user input via a multi-select menu
import inquirer

from game import play_game
from stats import view_stats, reset_stats


def main():
    """Main function to display the menu and handle user choices."""

    while True:
        questions = [
            inquirer.List(
                "choice",
                message="Select an option",
                choices=["Play Game", "View Stats", "Reset Stats", "Quit"],
            ),
        ]
        answer = inquirer.prompt(questions)

        if answer["choice"] == "Play Game":
            play_game()
        elif answer["choice"] == "View Stats":
            view_stats()
        elif answer["choice"] == "Reset Stats":
            reset_stats()
        elif answer["choice"] == "Quit":
            print("Goodbye!\n")
            break


if __name__ == "__main__":
    main()
