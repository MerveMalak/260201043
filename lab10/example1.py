def f(n):
  if n == 1: 
    return 3 
  return 3 + f(n-1)
print(f(8))