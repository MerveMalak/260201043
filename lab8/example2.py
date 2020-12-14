def is_prime(number):
  if number == 1:
    return False
  for i in range(1,number):
    if number % i == 0:
      return False
  return True

def print_primes_between(num1,num2):
  for i in range(num1,num2):
    if is_prime(i):
      print(i)
x = int(input("number1:"))
y = int(input("number2:"))
print_primes_between(x,y)