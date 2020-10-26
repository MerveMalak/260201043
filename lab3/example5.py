month = input("Enter a month: ").capitalize().strip()
day = int(input("Enter a day: "))

if (month == "March" and day >= 20) or (month=="April") or (month == "May") or (month == "June" and day < 21): 
  print("The season is Spring.")
elif (month == "June" and day >= 21) or (month == "July") or (month == "August") or (month == "September" and day < 22):
  print("The season is Summer.")
elif (month == "September" and day >= 22) or (month == "October") or (month == "November") or (month == "December" and day < 21):
  print("The season is Winter.")
else:
  print("The season is Fall.")