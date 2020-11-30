numbers1 = [2,3,4,20,5,5,15]
numbers2 = [10,20,20,15,30,40]
set_numbers1 = set(numbers1)
set_numbers2 = set(numbers2)
intersection_set = set()
union_set = set_numbers2
for i in numbers1:
  if i in numbers2:
    intersection_set.add(i)
  else:
    union_set.add(i)
print(intersection_set)
print(union_set)