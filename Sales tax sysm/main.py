# Sales Tax Challenge – Task Two (Day 1)
import tkinker as tk
# Declaring Variables
labor_cost_per_hour = 20.00
labour_hours_per_gallon = 8.0

# User query for input
area = float(input("Enter the square feet of wall space to be painted "))
paint_price = float(input("Enter price of the paint per gallon "))

gallons_required = area / 115
labor_hours = gallons_required * labour_hours_per_gallon
paint_cost = gallons_required * paint_price
labor_charges = labor_hours * labor_cost_per_hour
total_cost = paint_cost + labor_charges

# Program display
print("The number of gallons of paint required = ", gallons_required)
print("The hours of labor required = ", labor_hours )
print("The cost of the paint = $", gallons_required * paint_price)
print("The labor charges = $",labor_charges )
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
print("The Total Cost of the paint job = $",total_cost )
# after user has worked out and found an answer it would be nice to use tinker to say good bye
label = tk.Label(
    text="Hello, it was nice calculating the maths",
    foreground="white",  # Set the text color to white
    background="black"  # Set the background color to black
)

