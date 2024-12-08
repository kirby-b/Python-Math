# Initial value for the count of numbers in the equation. 
# This needs to be set to 0 initially to prevent errors
num_of_nums = 0 


def do_math():
    result = 0
    equation = input("Please enter your equation.\nThe supported operands are: */x, /, %, +, and -.\nIt must have spaces in between(Ex: 2 + 2 or 4 + 1 * 3):\n").lower()
    pieces = equation_to_array(equation)
    oper_index = 1
    next_num = 2
    global num_of_nums
    num1 = int(pieces[0]) # Num1 starts as the first index of pieces(should be a number)
    x = 0 # X starts as zero because if it inst assigned a number, it cant be compared against num_of_nums
    while x < num_of_nums: 
        # Due to looping for the count of numbers found in the equation, It completely ignores the final index if its an operand
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
        # Once the current equation evaluates, it shifts operation type and num2
        # by 2 indexs to get the new operand and number.
    print(f"{int(result):.2f}\n")


def equation_to_array(equation: str):
    global num_of_nums
    while True:
        pieces = remove_whitespace(equation)
        # Checks the input to make sure the list consists of numbers followed by operands.
        x = 0
        while x < len(pieces):
            if int(x) % 2 == 1: # Checks all odd indexes(should be operands)
                if pieces[int(x)] not in ["x", "*", "/", "-", "+", "%"]:
                    pieces = input("Invalid operation in input.\nPlease enter two numbers and a operation (Ex: 2 + 2), it must have spaces in between:").lower()
                    break
            if int(x) % 2 == 0: # Checks all even indexes(should be numbers)
                if not pieces[int(x)].isnumeric():
                    pieces = input("Input does not contain numbers.\nPlease enter two numbers and a operation (Ex: 2 + 2), it must have spaces in between:").lower()
                    break
                if x >= 2:
                    num_of_nums += 1
            x += 1
        break
    return pieces


def remove_whitespace(equation: str):
    x = 0
    no_whitespace = equation.split(" ")  # Splits the equation string, using spaces as a delimiter
    while x < len(no_whitespace):
        if no_whitespace[int(x)] == "" or no_whitespace[int(x)].isspace():
            no_whitespace.pop(int(x))  # Pops the index if it is empty or a space
        else:
            x += 1
    return no_whitespace
