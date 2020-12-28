def halistone(n):
  if n == 1:
    return "1"
  
  if n % 2 == 0:
    return str(int(n)) + "," + str(halistone(n/2))
  
  else:
    return str(int(n)) + "," + str(halistone(3*n + 1))
print(halistone(11))