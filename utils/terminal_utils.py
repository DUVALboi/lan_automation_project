import os
import sys

def clear_terminal():
    """Clears the terminal screen."""
    print("\n" * 100)

def get_input(prompt):
    """Prompts the user for input."""
    return input(prompt)

def print_output(output):
    """Prints output to the terminal."""
    print(output)

def exit_program():
    """Exits the program."""
    sys.exit(0)

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu(title, options):
    """Displays a menu with the given title and options.

    Args:
        title (str): The title of the menu.
        options (list): A list of strings representing the menu options.

    Returns:
        str: The user's choice.
    """
    while True:
        clear_screen()
        print(title)
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")
        choice = input("Enter choice: ")
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return choice
        else:
            print("Invalid choice. Please try again.")

def pause():
    """Pauses the program until the user presses Enter."""
    input("Press Enter to continue...")

# Example usage
if __name__ == "__main__":
    title = "Main Menu"
    options = ["Option 1", "Option 2", "Exit"]
    choice = display_menu(title, options)
    print(f"You selected: {choice}")
    pause()
