year = int(input("Enter a year:" ))
is_leap = True
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 != 0:
      is_leap = False
  else:
    is_leap = True
else:
  is_leap = False

if is_leap:
  print(f"{year} is leap year.")
else:
  print(f"{year} is not leap year.")