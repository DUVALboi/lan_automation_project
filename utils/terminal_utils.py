# utils/terminal_utils.py

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
