def binary_to_dec(number1):
  decimal = 0
  number1 = number1[::-1]
  for i in range(len(number1)):
    decimal += (2**i)* int(number1[i])
  return decimal
def decimal_to_bin(number2):
  binary = ""
  while number2 > 0:
    binary += str(number2%2)
    number2 //= 2
  return binary[::-1]
def main():
  number1 = "10010"
  print(binary_to_dec(number1))
  number2 = 18
  print(decimal_to_bin(number2))
main()