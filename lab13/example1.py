def selection_sort(nums):
  for i in range(len(nums)): 
    min_idx = i 
    for j in range(i+1, len(nums)): 
        if nums[min_idx] > nums[j]: 
            min_idx = j 
                       
    nums[i], nums[min_idx] = nums[min_idx], nums[i]
  return nums
nums = [1,4,3,5,2,9,6]
print(selection_sort(nums))
