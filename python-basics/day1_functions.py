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

# ---- Exercise 3: Reverse a string  ----
def string_reverser(s):
     reversed_string = ""
     for i in range(-1, -len(s)-1, -1):
          reversed_string += s[i]
     return reversed_string

# ---- Exercise 4: Even number  ----
def even(nums):
     even_list = []
     for i in range(len(nums)):
          if nums[i] % 2 == 0:
               even_list.append(nums[i])
     return even_list

# ---- Exercise 5: palindrome  ----
def palindrome(s):
     for i in range(len(s)//2):
          if s[i] != s[-i-1]:
               return False
     return True
          
# ---- Exercise 6: Common elements in two lists ----
def common_elements(l1, l2):
     common_list = []
     for i in range(len(l1)):
          for j in range(len(l2)):
               if l1[i] == l2[j]:
                    common_list.append(l1[i])
     return common_list

# ---- Exercise 7: Sort a list in ascending order ----
def sort_ascending(nums):
     for i in range(len(nums)):
          for j in range(i+1, len(nums)):
               if nums[i] > nums[j]:
                   temp = nums[i]
                   nums[i] = nums[j]
                   nums[j] = temp
     return nums



     



if __name__ == "__main__":
    print("Exercise1_output:", average([10, 20, 30]))
    print("Exercise2_output:", find_max([3, 7, 2, 9, 1]))
    print("Exercise3_output:", string_reverser("hello"))
    print("Exercise4_output:", even([1, 2, 3, 4, 5, 6]))
    print("Exercise5_output:", palindrome("racecar"))
    print("Exercise5_output:", palindrome("hello"))
    print("Exercise6_output:", common_elements([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))
    print("Exercise7_output:", sort_ascending([5, 3, 8, 1, 9, 2]))
  

