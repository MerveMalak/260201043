def pascal(n):
    if n == 1:
        return [[1]]
    else:
        line = [1]
        previousline = pascal(n-1)
        for i in range(len(previousline[-1])-1):
            line.append(previousline[-1][i]+ previousline[-1][i+1])
        line.append(1)
        return pascal(n-1) + [line]
print(pascal(3))