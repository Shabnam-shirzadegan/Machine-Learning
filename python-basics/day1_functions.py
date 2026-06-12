# ---- Exercise 1: Find average ----
def average(nums):
    sum = 0
    for i in range(len(nums)):
         sum += nums[i] 
    ave = sum / len(nums)
    # built-in sum() function
    # ave = sum(nums) / len(nums) 
    return ave


# ---- Exercise 2: Find largest number ----
def find_max(nums):
     max = nums[0]
     for i in range(len(nums) -1):
          if max < nums[i+1]:
               max = nums[i+1]
     return max





if __name__ == "__main__":
    print("Exercise1_output:", average([10, 20, 30]))
    print("Exercise2_output:", find_max([3, 7, 2, 9, 1]))