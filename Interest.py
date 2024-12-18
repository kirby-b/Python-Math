def get_interest():
    # Prompts the user for input values
    initial = input("Enter the initial amount: ")
    rate = input("Enter the interest rate(number percent, EX: 5): ")
    time = input("Enter the time in years(round): ")

    # Checks to make sure inputs are valid and asked for new input if needed
    while not time.isnumeric() or time <= 0 or not is_float(initial) or not is_float(rate):
        if not is_float(initial) or initial <= 0:
            print("Initial amount can not be less than or equal to zero")
            initial = float(input("Enter the initial amount: "))
        if not is_float(rate) or rate <= 0:
            print("Interest rate can not be less than or equal to zero")
            rate = float(input("Enter the interest rate: "))
        if not time.isnumeric() or time <= 0:
            print("Time passed can not be less than or equal to zero")
            time = int(input("Enter the time in years(round): "))
    # Gets all values and calculates interest
    total = float(initial) * pow((1 + float(rate) / 100), int(time))
    print(f"Balance after {time} year/s: ${total:.2f}\n")


# Custom function I made because using isinstance required me to add more code, in the end this was fewer lines.
def is_float(string):
    try:
        float(string)  # Turn the input into a float. If it is not a number or float, it will throw an exception
        return True
    except ValueError:  # On exception, it will return false
        return False
