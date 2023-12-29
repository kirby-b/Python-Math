class AreaOfObject:
    def measuring():
        shape = AreaOfObject.getShape()
        if shape == "triangle" or shape == "t":
            AreaOfObject.Triangle()
        if shape == "rectangle" or shape == "r":
            AreaOfObject.Rectangle()
        if shape == "circle" or shape == "c":
            AreaOfObject.Circle()
    def getShape():
        while True:
            print("""What Kind of shape would you like to measure:
                1.Rectangle
                2.Circle
                3.Triangle""")
            valid = input().lower().strip()
            if valid in ["rectangle", "r", "circle", "c", "triangle", "t"]:
                return valid
            else:
                print("Invalid input please input a shape or its first letter")
                
    def Triangle():#Calculates triangle area
        print("Input the base and height:")
        print("Base:")
        inp = str.strip(input())
        base = int(inp)
        print("Height:")
        inp = str.strip(input())
        height = int(inp)
        area = base * height
        print(f"The area is {area}\n")
    def Rectangle(): #Calculates square area
        print("Input the length and width:")
        print("Length:")
        inp = str.strip(input())
        length = int(inp)
        print("Width:")
        inp = str.strip(input())
        width = int(inp)
        area = length * width
        print(f"The area is {area}\n")
    def Circle():#Calculates circle area
        import math
        print("Input the radius:")
        print("Radius:")
        inp = str.strip(input())
        radius = int(inp)
        area = math.pi * pow(radius, 2)
        print(f"The area is {area}\n")
    