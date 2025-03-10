# Greet user
print("Welcome to the Tip Calculator!")

# Ask for the total bill
total = float(input("What was the total bill? $"))

# Ask for percentage to tip
tipPercentage = int(input("How much tip would you like to give? \n10, 12, 15, or 20?"))

# Ask for how many of their party size is splitting the bill
splitSize = int(input("How many people are splitting this bill?"))

# Perform calulations
eachPay = (total + (total * (tipPercentage/100))) / splitSize

# Print results rounded to the second decimal place
print(f"Each person should pay {round(eachPay,2)}")
