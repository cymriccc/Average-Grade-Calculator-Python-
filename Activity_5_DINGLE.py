from colorama import Fore, Style, init # type: ignore

init(autoreset=True)

ANSIcyan = '\033[96m'
ANSIreset = '\033[0m'
cyan = Fore.CYAN
bright = Style.BRIGHT
dim = Style.DIM
white = Fore.WHITE
yellow = Fore.YELLOW
reset = Style.RESET_ALL

print(cyan + bright + "=" * 38)
print(cyan + bright + "Activity 5: Average Grade Calculator (by DINGLE)" + reset)
print(cyan + bright + "==== Calculate your Average Grade ====" + reset)
print()
name = str(input(white + bright + "Enter name: " + cyan + dim + reset))
math = int(input(white + bright + "Grades in Math: " + cyan + dim + reset))
science = int(input(white + bright + "Grades in Science: " + cyan + dim + reset))
english = int(input(white + bright + "Grades in English: " + cyan + dim + reset))
filipino = int(input(white + bright + "Grades in Filipino: " + cyan + dim + reset))
average = (math + science + english + filipino) / 4
print()
print(cyan + bright + "Hello, " + yellow + bright + name + "! Your average grade is: " + ANSIcyan + str(average) + ANSIreset)