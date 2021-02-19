from os import system
import platform
from colorama import Fore, Back, Style

def clrscr():
    if platform.system() == "Windows":
        system("cls")
    else:
        system("clear")

def display():
    try:
        print(Fore.RED+''' _
| |_ _   _ _ __ ___  _ __   __ _ ___ ___
| __| | | | '_ ` _ \| '_ \ / _` / __/ __|
| |_| |_| | | | | | | |_) | (_| \__ \__ \\
 \__|\__, |_| |_| |_| .__/ \__,_|___/___/
     |___/          |_|
'''+Style.RESET_ALL)
    except (ModuleNotFoundError):
        system("pip install -r requirements.txt")
