import random

def get_rand_list(b,e):
  N = 5
  list1 = random.sample(range(b,e),N)
  list2 = random.sample(range(b,e),N)
  return list1, list2

def main():
  
  list1,list2 = get_rand_list(0,10)
  list1,list2 = set(list1),set(list2)
  print(list1.intersection(list2))
main()