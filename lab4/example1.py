number = int(input("Enter the number: "))
if number < 10 :
  total = number
else:
  last_digit = number%10
  two_digit = (number//10) % 10
  total = last_digit + two_digit
print("SUM:", total)
