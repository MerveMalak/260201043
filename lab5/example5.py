n = int(input("How many Fibonacci numbers to generate?: "))
a,b = 1,1
result = ""
for i in range(n):
    result = result + str(a) + ","
    a,b = b, (a+b)
print(result+"...")