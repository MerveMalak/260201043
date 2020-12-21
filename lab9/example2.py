def get_reversed(my_list):
  i = len(my_list)
  if len(my_list) == 0:
    return []
  else:
    return [my_list[i-1]] + get_reversed(my_list[:i-1])
print(get_reversed([1,2,3,4]))