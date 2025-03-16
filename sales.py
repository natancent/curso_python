# Input sales for each seller
print("Enter sales amount for Seller 1:")
sales1 = float(input())
print("Enter sales amount for Seller 2:")
sales2 = float(input())
print("Enter sales amount for Seller 3:")
sales3 = float(input())

# Calculate commissions (3% for each seller)
commission1 = sales1 * 0.03
commission2 = sales2 * 0.03
commission3 = sales3 * 0.03
total_commission = commission1 + commission2 + commission3

# Input store expenses
print("Enter store rent amount:")
rent = float(input())
print("Enter supplier payment amount:")
supplier_payment = float(input())
print("Enter utility bills amount (water and electricity):")
utilities = float(input())

# Calculate total revenue and total expenses
total_sales = sales1 + sales2 + sales3
total_expenses = total_commission + rent + supplier_payment + utilities

# Calculate profit
profit = total_sales - total_expenses

# Display results
print(f"Total Sales: {total_sales:.2f}")
print(f"Total Expenses: {total_expenses:.2f}")
print(f"Profit: {profit:.2f}")

# Check if business is profitabl
if profit > 0:
    print("The business is profitable!")
elif profit == 0:
    print("The business is breaking even.")
else:
    print("The business is running at a loss!")