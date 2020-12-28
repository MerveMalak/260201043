def pascal_last_line(n):
    if n == 1:
        return [1]
    else:
        line = [1]
        previousline = pascal_last_line(n-1)
        for i in range(len(previousline)-1):
            line.append(previousline[i]+ previousline[i+1])
        line.append(1)
    return line
print(pascal_last_line(3))