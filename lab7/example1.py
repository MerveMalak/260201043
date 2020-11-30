dict_exmple = dict((("Jon",15), ("Ned",45), ("Arya",9), ("Catelyn",44), ("Bran",10)))
print(dict_exmple)
for current_key in dict_exmple.keys():
  if(dict_exmple[current_key] > 18):
    print(current_key)