n = int(input("Enter a number: "))
matrix = []
for i in range(n):
    matrix.append([0]*n)
for i in range(len(matrix)):
    matrix[i][i] = 1
print(matrix)