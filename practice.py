
downPayment = 250000
epsilon = 100
salary = 12500
high = salary
low = 0
bisection_round = 0
best_saving_portion = (low + high) / 2
while abs((best_saving_portion * 36) - downPayment) > epsilon:
    if best_saving_portion * 36 > downPayment:
        high = best_saving_portion
    else:
        low = best_saving_portion
    bisection_round += 1
    best_saving_portion = (low + high) / 2
answer = best_saving_portion / salary

print(best_saving_portion)
print(bisection_round)
print(round(answer, 4))
