class Interest:
    
    def getInterest():
        initial = 0
        rate = 0
        time = 0

        while initial <= 0:
            initial = float(input("Enter the initial amount: "))
            if initial <= 0:
                print("Inital amount can not be less than or equal to zero")

        while rate <= 0:
            rate = float(input("Enter the interest rate: "))
            if rate <= 0:
                print("Interest rate can not be less than or equal to zero")

        while time <= 0:
            time = int(input("Enter the time in years: "))
            if time <= 0:
                print("Time passed can not be less than or equal to zero")

        total = initial * pow((1 + rate / 100), time)
        print(f"Balance after {time} year/s: ${total:.2f}\n")