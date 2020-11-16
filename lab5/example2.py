number = int(input("How many numbers?: "))
even_counter = 0
for i in range(number):
    num = int(input("Enter a integer: "))
    if num % 2 == 0:
        even_counter += 1
print(even_counter/number, "%")