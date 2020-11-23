number_list = list(map(int,input("Enter numbers(use a comma): ").split(",")))
unique_list = list(set(number_list))
print(sorted(unique_list, reverse = True))