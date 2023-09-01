def cal_median(nums):
  nums.sort()
  n = len(nums)
  m = n // 2
  print(m)
  if n % 2 == 0:
    return (nums[m - 1] + nums[m]) / 2
  else:
    return nums[m]
print(cal_median([1,2,3,4,5]))
print(cal_median([1,2,3,4,5,6]))
