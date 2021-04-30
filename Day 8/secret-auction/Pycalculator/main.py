import os
from art import logo

def clear():
    os.system('cls') #Clears the all previous outputs

print(logo)
print("Welcome to my PyCalculator!")

def calculator():
  first_num = float(input("Enter the first number: "))

  if first_num - int(first_num) == 0:
    first_num = int(first_num)

  while True:
    
    operation = input("*\n/\n+\n-\nPick an operation: ")
    second_num = float(input("What's the next number: "))
    
    if  second_num - int(second_num):
      second_num = int(second_num)
    #operation
    if operation == "*":
      answer = first_num * second_num
    elif operation == "/":
      answer = first_num / second_num
    elif operation == "+":
      answer = first_num + second_num
    elif operation == "-":
      answer = first_num - second_num
    else:
      print("You provided invalid operation.")
      continue
    result = answer
    if result - int(result) ==0:
      result = int(result)
    print(f"{first_num} {operation} {second_num} = {result}")

    ask_continue = input(f"Type 'y' to continue with {answer}, or type 'n' to start new calculation: ")

    if ask_continue == "n":
      clear()
      calculator()
    elif ask_continue == "y":
      first_num = result
    else :
      break

calculator()
