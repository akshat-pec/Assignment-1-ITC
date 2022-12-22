print("Calculate your Income Tax")
a = int(input("Enter your Gross Income: "))
# a is Gross Income here
b = int(input("Enter Number of Dependants: "))
# b is Number of Dependants here
print("You have standard deduction of $10,000")
c = 10000
# c is standard deduction
d = 3000
# d is dependant deduction per dependant
e = b*d
# e is total dependant deduction
print("You have $3,000 as per dependant deduction i.e. $" , (e))
f = a-c-e
# f is Taxable income
print("Your Taxable income is $" ,(f))
g = 0.20
# g is the flat tax rate
print("All taxpayers are charged a flat tax rate of 20%.")
h = int(f*g)
# h is the Income Tax
print("Your Income Tax is $" ,(h))