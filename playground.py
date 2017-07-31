def same_first_last(nums):
  first = nums[0]
  last = nums[len(nums) - 1]
  if len(nums) >= 1 and first is last:
      print('True')
  else:
      print('False')

same_first_last([1, 2, 3])
same_first_last([1, 2, 3, 1])
same_first_last([1, 2, 1])