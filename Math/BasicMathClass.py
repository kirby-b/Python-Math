class BasicMath:

    def math():
        print("""Please enter two numbers, note this program works like a calculator so make sure you
    enter your numbers in the correct order""")
        print("Number 1:")#Gets the first number
        inp = str.strip(input())
        num1 = float(inp)
        print("Number 2:")#Gets the second number
        inp = str.strip(input())
        num2 = float(inp)
        op = BasicMath.getOperation()#Gets operation
        if op == "a" or op == "addition":
            result = num1 + num2
        if op == "s" or op == "subtraction":
            result = num1 - num2
        if op == "m" or op == "multiplication":
            result = num1 * num2
        if op == "d" or op == "division":
            result = num1 / num2
        if op == "r" or op == "remainder":
            result = num1 % num2 
        print(f"{result:.2f}\n")
    
    def getOperation(): #Gets operation type
        while True:
            print("""Now please input a type of operation.
            Acceptable operations are:
            Multiplication
            Division
            Addition
            Subtraction
            Remainder(modulus)""")
            operation = input().lower().strip()
            #Validates input
            if operation in ["multiplication", "m", "division", "d", "addition", "a", "subtraction", "s", "remainder", "r"]:
                return operation
            else:
                print("Invalid input please an operation type or its first letter")
