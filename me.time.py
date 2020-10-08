def getDreamHouse():
    # Assumptions
    semi_annual_raise = 0.07
    house_cost = 1000000
    down_Payment = house_cost * 0.25
    annual_salary = int(input("Enter your annual salary: "))
    salary = annual_salary / 12
    bank_return = 0.04
    low = 0
    high = 100
    guess = (low + high) / 2
    bisection_round = 0

    # salary raise function

    def liveFor36Months(monthly_salary, save_rate):
        current_save = 0
        for month in range(36):
            if month % 6 == 0 and month != 0:
                monthly_salary += monthly_salary * semi_annual_raise
            current_save += current_save * (bank_return / 12)
            current_save += monthly_salary * (save_rate / 100)
        return current_save

    if liveFor36Months(salary, 100) < down_Payment:
        print("It is not possible to pay the down payment in three years")
    else:
        while abs(liveFor36Months(salary, guess) - down_Payment) > 100:
            if liveFor36Months(salary, guess) < down_Payment:
                low = guess
            else:
                high = guess
            guess = (low + high) / 2
            bisection_round += 1

        print("steps in bisection search:", bisection_round)
        print("the best saving rate is", round(guess / 100, 4), "a month")


getDreamHouse()
