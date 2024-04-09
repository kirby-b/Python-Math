def do_math():
    result = 0
    pieces = []
    equation = input("Please enter two numbers and a operation (Ex: 2 + 2), it must have spaces in between:").lower()
    pieces = equation_to_array(equation)
    oper_type = pieces[1]
    num1 = pieces[0]
    num2 = pieces[2]
    if op == "+":
        result = num1 + num2
    if op == "-":
        result = num1 - num2
    if op == "x" or op == "*":
        result = num1 * num2
    if op == "/":
        result = num1 / num2
    if op == "%":
        result = num1 % num2
    print(f"{result:.2f}\n")


def equation_to_array(equation: str):  # Gets operation type
    pieces = []
    while True:
        pieces = remove_whitespace(equation)
        # Validates input
        if equation[1] not in ["x", "*", "/", "-", "+", "%"]:
            equation = input("Invalid operation in input.\nPlease enter two numbers and a operation (Ex: 2 + 2), it must have spaces in between:").lower()
        elif equation[0].isnumeric() == False or equation[2].isnumeric() == False:
            equation = input("Input does not contain numbers.\nPlease enter two numbers and a operation (Ex: 2 + 2), it must have spaces in between:").lower()
        else:
            break
    return pieces

def remove_whitespace(equation: str):
    x = 0
    no_whitespace = equation.split(" ")
    while x < len(no_whitespace):
        if no_whitespace[x] == "" or no_whitespace[x].isspace():
            no_whitespace.pop(x)  # Pops the index if it is empty or a space
        else:
            x += 1
    return no_whitespace