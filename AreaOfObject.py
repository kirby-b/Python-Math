import math  # Imports the math module to access the pi and pow functions


def measuring():
    shape = get_shape()
    if shape == "triangle" or shape == "t":
        triangle()
    if shape == "rectangle" or shape == "r":
        rectangle()
    if shape == "circle" or shape == "c":
        circle()


def get_shape():
    while True:
        # Prompts the user for what shape they want to calculate
        print("""What Kind of shape would you like to measure:
            1.Rectangle
            2.Circle
            3.Triangle""")
        valid = input().lower().strip()  # Formats the input to prevent errors
        # Checks the input to make sure it is a valid shape
        if valid in ["rectangle", "r", "circle", "c", "triangle", "t"]:
            return valid
        else:
            print("Invalid input please input a shape or its first letter")


def triangle():  # Calculates triangle area
    print("Input the base and height:")
    print("Base:")
    inp = str.strip(input()) 
    base = int(inp)
    print("Height:")
    inp = str.strip(input())
    height = int(inp)
    area = base * height
    print(f"The area is {area}\n")


def rectangle():  # Calculates square area
    print("Input the length and width:")
    print("Length:")
    inp = str.strip(input())
    length = int(inp)
    print("Width:")
    inp = str.strip(input())
    width = int(inp)
    area = length * width
    print(f"The area is {area}\n")


def circle():  # Calculates circle area
    print("Input the radius:")
    print("Radius:")
    inp = str.strip(input())
    radius = int(inp)
    # Circle needs the math.pi and pow functions
    area = math.pi * pow(radius, 2)
    print(f"The area is {area}\n")
