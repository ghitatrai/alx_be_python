monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))

monthly_savings = monthly_income - monthly_expenses
print(f"Your monthly saving are §{monthly_savings}")

annual_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print(f"Projected savings after one year, with interest, is: ${annual_savings}")
