# utils.py
import os

def clear_screen():
    """
    Clears the console screen for better readability.
    Works on both Windows and Unix-based systems.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
