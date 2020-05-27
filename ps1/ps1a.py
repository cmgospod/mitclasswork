def house_hunting(annual_salary, portion_saved, total_cost):
    monthly_savings = (annual_salary/12) * portion_saved
    total_savings = 0
    time = 0
    down_payment = total_cost/4
    while total_savings < down_payment:
        total_savings *= 1 + (.04/12)
        total_savings += monthly_savings
        time += 1
    return time
salary = float(input('Enter your annual salary'))
save = float(input('Enter the percent of your salary to save, as a decimal'))
house = float(input("Enter the cost of your dream home"))
print(house_hunting(salary, save, house))