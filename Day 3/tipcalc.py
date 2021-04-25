from decimal import *

print("Welcome to the tip calculator!")

total_bill = float(input("What was the total bill? $"))

numbofpeople = float(input("How many people to split the bill? "))

tip_percent = float(input("What percentage would you like to give? 10, 12 or 15? "))

eachpay = total_bill*(1+tip_percent/100) / numbofpeople

print("Each person should pay: $", round(eachpay, 2))
