num1 = int(input("Enter a number 1: "))
num2 = int(input("Enter a number 2: "))
matching_digit = 0
for i in range(min(len(str(num1)),len(str(num2)))):
    if num1 % 10 == num2 % 10:
        matching_digit += 1
    num1 //= 10
    num2 //= 10
print(matching_digit)