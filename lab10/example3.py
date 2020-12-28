def sum_list(my_list):
  if len(my_list) == 0:
    return 0
  if isinstance(my_list[0], list):
    return sum_list(my_list[0]) + sum_list(my_list[1:])
  else:
    return my_list[0] + sum_list(my_list[1:])
        

print(sum_list([3,12,76,[4,56,43],[2,8],81,75]))