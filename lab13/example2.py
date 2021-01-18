def binarySearch(alist, item):

  if len(alist) == 0:

    return -1

  else:

    midpoint = len(alist)//2

    if alist[midpoint] == item:

      return midpoint

    elif item < alist[midpoint]:

      return binarySearch(alist[:midpoint], item)

    else:

      location = binarySearch(alist[midpoint+1:], item)
      if location == -1:
        return location
      else:
        location = location + midpoint +1
        return location
nums = [1,4,3,5,2,9,6]
nums.sort()
print(binarySearch(nums,9))