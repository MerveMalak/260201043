n = int(input("Enter a number: "))
matrix = []
for i in range(n):
  row = list(map(int, input(f"Enter a {n} number(use a comma): ").split(",")))
  matrix.append(row)
trace = 0
for i in range(len(matrix)):
  trace = trace + matrix [i][i]
print(trace)
