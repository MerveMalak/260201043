def hailstone(n):
  if n == 1:
    return "1"
  
  if n % 2 == 0:
    return str(int(n)) + "," + str(hailstone(n/2))
  
  else:
    return str(int(n)) + "," + str(hailstone(3*n + 1))
print(hailstone(11))