number = int(input("Enter a integer: "))
while True:
  if number < 0:
    print("Please enter valid number: ")
    number = int(input("Enter a integer: "))
  elif number > 10:
    print("Please enter number <10: ")
    number = int(input("Enter a integer: "))
  else:
    for i in range(1,11):
      print(f"{number} * {i} = {number * i}")
    break