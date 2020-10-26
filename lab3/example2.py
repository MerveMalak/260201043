num1 = int(input("Enter number 1 :"))
num2 = int(input("Enter number 2 :"))
num3 = int(input("Enter number 3 :"))

if num2 < num1 and num3 < num1:
  max_num = num1
  
elif num1 < num2 and num3 < num2:
  max_num = num2
else:
  max_num = num3
print(max_num)

