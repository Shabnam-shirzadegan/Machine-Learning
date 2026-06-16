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

# ---- Exercise 8: Count each character in a string ----
def count_char(s):
    output_dict = {}
    for i in range(len(s)):
        if s[i] in output_dict:
            output_dict[s[i]] += 1
        else:
            output_dict[s[i]] = 1
    return output_dict

# ---- Exercise 8b: Check for duplicates in a list ----
def duplicates_check(s):
     temp_dict = {}
     for i in range(len(s)):
          if s[i] in temp_dict: 
               return True
          else:
               temp_dict[s[i]] = 1
     return False
     
# ---- Exercise 8c: Find first non-repeated character in a string ----
def nonrepeated(s):
     dict = {}
     for i in range(len(s)):
          if s[i] in dict:
               dict[s[i]] += 1
          else:
               dict[s[i]] = 1
     for key in dict:
               if dict[key] == 1:
                    return key
     
# ---- Exercise 9: Group words by their first letter ----
def group_by_first_letter(words):
     dict = {}
     for word in words:
           if word[0] in dict:
                dict[word[0]].append(word)  
           else:
                dict[word[0]] = [word]
     return dict

# ---- Exercise 10: Count word frequency in a sentence ----
def word_counter(s):
     dict= {}
     words = s.split()
     for word in words:
          if word in dict:
               dict[word] += 1
          else:
               dict[word] = 1
     return dict

# ---- Exercise 11: Find two numbers that add up to a target ----
def two_sum(nums, target):
     for i in range(len(nums)-1):
          for j in range(i+1, len(nums)):
               if nums[i] + nums[j] == target:
                    return [nums[i] , nums[j]]
                    
# ---- Exercise 11b: Two sum using hash map ----
def two_sum_hash(nums, target):
     dict = {}
     for number in nums:
          number2 = target - number
          if number2 in dict:
               return [number, number2]
          else:
               dict[number] = 1 

# ---- Exercise 12: Find the most frequent element in a list ----
def most_frequent(nums):
     dict = {}
     max_count = 0 
     max_key = None
     for number in nums:
          if number in dict:
               dict[number] += 1
          else:
               dict[number] = 1             
     for key in dict:
          if max_count < dict[key]:
               max_count = dict[key]
               max_key = key
     return max_key

# ---- Exercise 13: FizzBuzz ----
def fizzbuzz(n):
     result = []
     for value in range(1,n+1):
          if value % 3 == 0 and value % 5 == 0:
               result.append("FizzBuzz")
          elif value % 3 == 0:
               result.append("Fizz")
          elif value % 5 == 0:
               result.append("Buzz")
          else:
               result.append(value)
     return result

# ---- Exercise 14: Flatten a nested list ----
def flatter(nums):
     flatten_list = []
     for i in range(len(nums)):
          for j in range(len(nums[i])):
               flatten_list.append(nums[i][j])
     return flatten_list




if __name__ == "__main__":
    print("Exercise1_output:", average([10, 20, 30]))
    print("Exercise2_output:", find_max([3, 7, 2, 9, 1]))
    print("Exercise3_output:", string_reverser("hello"))
    print("Exercise4_output:", even([1, 2, 3, 4, 5, 6]))
    print("Exercise5_output:", palindrome("racecar"))
    print("Exercise5_output:", palindrome("hello"))
    print("Exercise6_output:", common_elements([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))
    print("Exercise7_output:", sort_ascending([5, 3, 8, 1, 9, 2]))
    print("Exercise8_output:", count_char("hello"))
    print("Exercise8b_output:", duplicates_check([1, 2, 3, 4, 2]))
    print("Exercise8b_output:", duplicates_check([1, 2, 3, 4, 5]))
    print("Exercise8c_output:", nonrepeated("aabbcde"))
    print("Exercise9_output:", group_by_first_letter(["apple", "banana", "avocado", "blueberry", "cherry"]))
    print("Exercise10_output:", word_counter("the cat sat on the mat the cat"))
    print("Exercise11_output:", two_sum([2, 7, 11, 15], 9))
    print("Exercise11b_output:", two_sum_hash([2, 7, 11, 15], 9))
    print("Exercise12_output:", most_frequent([1, 3, 2, 3, 4, 3, 2]))
    print("Exercise13_output:", fizzbuzz(15))
    print("Exercise14_output:", flatter([[1, 2], [3, 4], [5, 6]]))




  

