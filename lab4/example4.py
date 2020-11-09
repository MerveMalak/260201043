a = int(input("The base number: "))
b = int(input("The power number: "))
total = 1
if b == 0:
    print("Result:1")
for i in range(abs(b)):
    if b > 0:
        total  *= a
    elif b < 0:
        total  *= (1/a)
print("Result:",total)