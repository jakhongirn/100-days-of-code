#Write your code below this line 👇
import math
def prime_checker(number):

  try:
    number = float(number)

    if number == int(number):
      number = math.trunc(number)
      if number > 1:
        for i in range(2, number):
          if number % i == 0:
            print("It's not a prime number.")
            break
        else :
          print("It's a prime number.")
      elif number < 0 :
        print("You've entered a negative number.")
      elif number==0 or 1:
        print(f'{number} is not a prime number.')
    else :
      print("Yo've entered a float type number.")

  except :
     print("You've entered not a number")
    



#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = input("Check this number: ")
prime_checker(number=n)



