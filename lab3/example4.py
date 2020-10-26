age = int(input("Enter your age: "))
normal_price = 3
if age < 6 or age > 60:
  print("It is free")
elif 6<= age <= 18:
  normal_price = normal_price - (normal_price*0.5)
  print(normal_price)
else:
  print(normal_price)
 