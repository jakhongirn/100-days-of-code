def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        print("Leap year")
      else:
        print("Not leap year.")
    else: 
      print("Leap year.")
  else: 
    print("Not leap year.")

entered_year = int(input("Enter a year: "))

is_leap(entered_year)