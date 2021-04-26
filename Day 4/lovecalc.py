# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

lname1 = name1.lower()
lname2 = name2.lower()

pairnames = lname1+lname2
t = pairnames.count('t')
r = pairnames.count('r')
u = pairnames.count('u')
e = pairnames.count('e')

true = int(t) + int(r) + int(u) +int(e)

l = pairnames.count('l')
o = pairnames.count('o')
v = pairnames.count('v')
e = pairnames.count('e')

love = int(l) + int(o) + int(v) +int(e)

truelove_score = str(true) + str(love)
truelove_score = int(truelove_score)


if truelove_score < 10 or truelove_score > 90:
  print(f"Your score is {truelove_score}, you go together like coke and mentos ;))")
elif truelove_score > 40 and truelove_score < 50:
  print(f"Your score is {truelove_score}, you are alright together.")
else : 
  print(f"Your score is {truelove_score}.")