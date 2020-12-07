# Pizza cost calculator

# How many pizzas they want
number_of_pizzas=eval(input("how many pizzas do you want? "))

# Cost of each pizza
cost_per_pizza=eval(input("how much does each pizza cost? "))

# Calculate the total cost of the pizzas as our subtotal
subtotal=number_of_pizzas*cost_per_pizza

# Calculate sales tax owed, at 8% of the subtotal
tax_percent=0.08
tax=subtotal*tax_percent

# Add the sales tax to the subtotal for the final total
total=subtotal+tax

# Show the user the total amount due, including tax
print("Your order costs", total, "dollars")
print("Sales tax is", tax, "becouse sales tax in our contry is", tax_percent)
