a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

delta = (b**2) - (4*a*c)
if delta > 0:
  print("There are two real roots.")
elif delta == 0:
  print("There is one real root.")
else:
  print("There are two complex roots.")
