n = int(input("Enter a number: "))
result = 1
for i in range(n,1,-1):
  result *= i
print(f"{n}! = {result}")