def even_number(my_list):
  if len(my_list) == 0:
    return 0
  elif my_list[-1] % 2 == 0:
    my_list.pop()
    return 1 + even_number(my_list)
  else:
      my_list.pop()
      return even_number(my_list)
print(even_number([0,1,2,3,4,5]))