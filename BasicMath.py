import math 

num_of_nums = 0

def do_math():
    result = 0
    pieces = []
    equation = input("Please enter your equation.\nThe supported operands are: */x, /, %, +, and -.\nIt must have spaces in between(Ex: 2 + 2 or 4 + 1 * 3):\n").lower()
    pieces = equation_to_array(equation)
    oper_index = 1
    next_num = 2
    global num_of_nums
    num1 = int(pieces[0])
    # Make it so you can have multiple numbers. Maybe go to next by adding 2 to num2 and oper_type
    x = 0
    while x < num_of_nums:
        oper_type = pieces[oper_index]
        num2 = int(pieces[next_num]) 
        if oper_type == "+":
            result = num1 + num2
        if oper_type == "-":
            result = num1 - num2
        if oper_type == "x" or oper_type == "*":
            result = num1 * num2
        if oper_type == "/":
            result = num1 / num2
        if oper_type == "%":
            result = num1 % num2
        x += 1
        oper_index += 2
        next_num += 2
        num1 = result
    print(f"{int(result):.2f}\n")


def equation_to_array(equation: str):  # Gets operation type
    # Find way to get multiple numbers and operands
    pieces = []
    global num_of_nums
    while True:
        pieces = remove_whitespace(equation)
        # Validates input
        x = 0
        while x < len(pieces):
            if int(x) % 2 == 1 :
                if pieces[int(x)] not in ["x", "*", "/", "-", "+", "%"]:
                    pieces = input("Invalid operation in input.\nPlease enter two numbers and a operation (Ex: 2 + 2), it must have spaces in between:").lower()
                    break
            if int(x) % 2 == 0:
                if pieces[int(x)].isnumeric() == False:
                    pieces = input("Input does not contain numbers.\nPlease enter two numbers and a operation (Ex: 2 + 2), it must have spaces in between:").lower()
                    break
                if x >= 2:
                    num_of_nums += 1
            x += 1
        break
    return pieces

def remove_whitespace(equation: str):
    x = 0
    no_whitespace = equation.split(" ") # Splits the string into an array at spaces
    while x < len(no_whitespace):
        if no_whitespace[int(x)] == "" or no_whitespace[int(x)].isspace():
            no_whitespace.pop(int(x))  # Pops the index if it is empty or a space
        else:
            x += 1
    return no_whitespace