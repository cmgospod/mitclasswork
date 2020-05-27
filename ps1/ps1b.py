def house_hunting(annual_salary, portion_saved, total_cost, semi_annual_raise):
    monthly_savings = (annual_salary/12) * portion_saved
    total_savings = 0
    time = 0
    down_payment = total_cost/4
    while total_savings < down_payment:
        total_savings *= 1 + (.04/12)
        total_savings += monthly_savings
        time += 1
        if time % 6 == 0:
            annual_salary *= 1 + semi_annual_raise
            monthly_savings = (annual_salary/12) * portion_saved
    return time
salary = float(input('Enter your annual salary'))
save = float(input('Enter the percent of your salary to save, as a decimal'))
house = float(input("Enter the cost of your dream home"))
raising = float(input("Enter the semi-annual raise, as a decimal"))
print(house_hunting(salary, save, house, raising))