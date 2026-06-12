def average(nums):
    sum = 0
    for i in range(len(nums)):
         sum += nums[i] 
    ave = sum / len(nums)
    # built-in sum() function
    # ave = sum(nums) / len(nums) 
    return ave
print(average([10, 20, 30]))
