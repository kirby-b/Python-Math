# Imports the classes from the other files.
from BasicMathClass import do_math
from InterestClass import get_interest
from AreaOfObjectClass import measuring


def main():
    print("Welcome to my math program.")

    while True:
        try:  # Tries to ask for input
            inp = str.strip(input("""Please input what kind of math you would like to do (use the numbers):
            1. Interest
            2. Basic math operations
            3. Area of 2d shapes"""))
            # Gets which math program to run and runs it
            while inp.isdigit() is False or inp not in ["1", "2", "3"]:
                print("Invalid input try again")
                inp = str.strip(input())
                # Validates the input
            if int(inp) == 1:
                get_interest()
            elif int(inp) == 2:
                do_math()
            elif int(inp) == 3:
                measuring()
        except KeyboardInterrupt:  # Catches a keyboard interrupt
            print("Shutting Down...")


if __name__ == "__main__":
    main()
