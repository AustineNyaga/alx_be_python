monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Project annual savings with interest
annual_savings = monthly_savings * 12  # Total savings for the year
projected_savings = annual_savings + (annual_savings * 0.05)  # Adding 5% annual interest

# Display the results
print(f"Your monthly savings are: ${monthly_savings:.2f}")
print(f"Your projected annual savings with interest are: ${projected_savings:.2f}")
