bill = float(input("How muc is the meal ?"))
tax = float(input("What is the sales tax (percentage)"))
tip = float(input("How much of a tip (percentage)"))

tax_amount = bill * tax / 100 # calculate the tax
total = bill + tax_amount # add tax amount to the final bill

tip_amount = (total * tip) / 100 # calculate the tip
total = total + tip_amount

total = round(total, 2) # Round tje total amount

print("The total bill is $ {}".format(total))
