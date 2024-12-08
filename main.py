# Imports my math class files so their functions can be used.
from BasicMath import do_math
from Interest import get_interest
from AreaOfObject import measuring


def main():
    print("Welcome to my math program.")

    while True:
        try:  # Prompts the user so they know what their choices are and how to respond.
            inp = str.strip(input("""Please input what kind of math you would like to do (use the numbers):
            1. Interest
            2. Basic math operations
            3. Area of 2d shapes\n"""))
            # Gets the users input so the program know what to run.
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
        except KeyboardInterrupt:  # Catches a keyboard interrupt so the user has a way to easily stop the program
            print("Shutting Down...")


if __name__ == "__main__":
    main()
