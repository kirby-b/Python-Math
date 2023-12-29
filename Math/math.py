
from BasicMathClass import BasicMath
from InterestClass import Interest
from AreaOfObjectClass import AreaOfObject
end = False

def main():
    print("Welcome to my math program.")

    while end == False: 
        print("""Please input what kind of math you would like to do (use the numbers):
        1. Interest
        2. Basic math operations
        3. Area of 2d shapes""")
        #Gets which math program to run and runs it
        inp = str.strip(input())
        while inp.isdigit() == False:
            print("Invalid input try again")
            inp = str.strip(input())
        if int(inp) == 1:
            Interest.getInterest()
        if int(inp) == 2:
            BasicMath.math()
        if int(inp) == 3:
            AreaOfObject.measuring()
            
if __name__ == "__main__":
    main()