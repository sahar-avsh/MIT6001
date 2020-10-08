def getDreamHouse():
    # Assumptions
    semi_annual_raise = 0.07
    annual_bank_return = 0.04
    cost_of_dream_house = 1000000
    down_payment = cost_of_dream_house * 0.25
    months = 36

    # Get necessary inputs
    annual_salary = int(input('Enter starting salary: '))
    salary = annual_salary / 12

    # Bi-section search
    high = 10000
    low = 0
    guess = (high + low) / 2
    counter = 0
    current_saving = 0
    epsilon = 100

    def simulation(salary, saving_rate):
        savings = 0
        for month in range(months):
            # bank return on savings
            savings += savings * (annual_bank_return / 12)

            # saving on salary
            savings += salary * (saving_rate / 10000)

            # semi-annual salary raise
            if (month + 1) % 6 == 0 and month != 0:
                salary += salary * semi_annual_raise

        return savings

    if simulation(salary, 10000) < down_payment:
        print('It is not possible to pay the down payment in three years.')
    else:
        while abs(current_saving - down_payment) > epsilon:
            # run the simulation
            current_saving = simulation(salary, guess)

            # update on high and low for bisection search
            if current_saving < down_payment:
                low = guess
            else:
                high = guess

            # update guess
            guess = (high + low) / 2

            # bisection round counter
            counter += 1

        # print out the results
        print('Best savings rate: ', round(guess / 10000.0, 4))
        print('Steps in bisection search: ', counter)


getDreamHouse()
