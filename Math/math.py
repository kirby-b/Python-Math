#Imports the classes from the other files.
from BasicMathClass import BasicMath
from InterestClass import Interest
from AreaOfObjectClass import AreaOfObject

def main():
    print("Welcome to my math program.")

    while True: 
        try: #Tries to ask for input
            inp = str.strip(input("""Please input what kind of math you would like to do (use the numbers):
            1. Interest
            2. Basic math operations
            3. Area of 2d shapes"""))
            #Gets which math program to run and runs it
            while inp.isdigit() == False or inp not in ["1", "2", "3"]:
                print("Invalid input try again")
                inp = str.strip(input())
                #Validates the input
            if int(inp) == 1:
                Interest.getInterest()
            elif int(inp) == 2:
                BasicMath.math()
            elif int(inp) == 3:
                AreaOfObject.measuring()
        except(KeyboardInterrupt): #Catches a keyboard interupt
            print("Shutting Down...")
            
if __name__ == "__main__":
    main()
