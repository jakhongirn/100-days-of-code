import math
#First *fork* your copy. Then copy-paste your code below this line 👇
#Finally click "Run" to execute the tests

def prime_checker(number):
  if number>1:  
    for i in range(2, number):
      if number%i == 0:
        print(f"{number} is not a prime number.")
        break

    else :
      print(f"{number} is a prime number")
  elif number==0 or 1 :
    print(f"{number} is not a prime number.")
  else:
    print("You've entered negative number")


#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
