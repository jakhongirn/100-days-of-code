from art import logo

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiplicate(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiplicate,
    "/": divide 
}

def calculator():
  print(logo)
  n1 = float(input("What's the first number?: "))

  for symbol in operations:
    print(symbol)
  should_continue = True

  while should_continue:
    operation = input("Pick an operation: ")

    n2 = float(input("What's the next number?: "))


    calculation_function = operations[operation]
    answer = calculation_function(n1, n2)

    print(f"{n1} {operation} {n2} = {answer} ")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ") == "y":
      n1 = answer
    else:
      should_continue = False
      
  
  
calculator()


