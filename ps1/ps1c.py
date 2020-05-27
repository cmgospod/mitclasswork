starting_salary = float(input("Enter your starting salary"))
poss = list(range(10001))
total_savings = 0
pointer = poss[len(poss) // 2]
saving_rate = float(pointer) / 10000
steps = 0
        
def saving(starting_salary, rate):
    monthly_savings = starting_salary * rate / 120000
    total_savings = 0
    for _ in range(6):
        for _ in range(6):
            total_savings *= 1 + (.04/12)
            total_savings += monthly_savings
        starting_salary *= 1.07
        monthly_savings = starting_salary * rate / 120000
    return total_savings

while True:
    steps += 1
    result = saving(starting_salary, pointer)
    if result < 249900:
        poss = poss[len(poss) // 2:]
        if len(poss) == 2:
            pointer = poss[0]
        else:
            pointer = poss[len(poss) // 2]
        if pointer == 10000:
            print("It is not possible to pay the down payment in three years")
            break
    elif result > 250100:
        poss = poss[:len(poss) // 2]
        if len(poss) == 2:
            pointer = poss[0]
        else:
            pointer = poss[len(poss) // 2]
    else:
        print(f'Best savings rate: {pointer/10000}')
        print(f'Steps in bisection search: {steps}')
        break