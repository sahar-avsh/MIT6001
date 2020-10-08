def getDreamHouse():
    import math
    annual_salary = int(input("Type your starting annual salary: "))
    semi_annual_raise = float(input("Type your semi annual raise in decimal form: "))
    portion_saved = float(input("Type how much you want to save per month in decimal form: "))
    total_cost = int(input("Type the price of your dream house:  "))
    downPayment = total_cost * 0.25
    salary = annual_salary / 12
    currentSaving = 0
    monthPassed = 0
    annualReturn = 0.04
    while currentSaving < downPayment:
        if monthPassed % 6 == 0 and monthPassed != 0:
            raised_salary = salary * semi_annual_raise
            salary += raised_salary
        monthly_save = salary * portion_saved
        monthPassed += 1
        bankReturn = currentSaving * (annualReturn / 12)
        currentSaving += bankReturn
        currentSaving += monthly_save
    print('Number of months: ', monthPassed)
    print('Number of year(s)-month(s): ', math.floor(monthPassed / 12), 'year(s)', monthPassed % 12, 'month(s)')


getDreamHouse()