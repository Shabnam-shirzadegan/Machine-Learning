#two_sum: brutal_force
def two_sum(nums, target):
    #result = [] if we wnat to store all the pairs that add up to the target 
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
               #result.append([i,j])
               #return result
                  return([i,j])
print (two_sum([2,7,11,15], 9))

#duplicate
def duplicate(nums):
     for i in range(len(nums)):
          for j in range(i+1, len(nums)):
               if nums[i] == nums [j]:
                    return True
     return False             
print(duplicate([1, 2, 3, 1]))  # True
print(duplicate([1, 2, 3, 4]))  # False

#anagram
def anagram(s, t):
     if len(s) != len(t):
          return False
     return sorted(s) == sorted(t)    
print(anagram("rat","tar")) 
print(anagram("rat","car")) 

#Palindrome 
def palindrom(s):
  no_space = "" 
  for char in s:
       if char.isalnum():
            no_space += char.lower()
  return no_space == no_space[::-1]
print(palindrom("racecar"))  
print(palindrom("Hello")) 
print(palindrom("A man a plan a canal Panama")) 

#Longest Substring
def long_sub(s):
     max_len= 0
     
     for i in range(len(s)):
          sub = s[i]
          for j in range(i+1, len(s)):
               if s[j] in sub:
                    break 
               sub += s[j]  
          max_len = max(max_len, len(sub))
     return max_len
print(long_sub("abcabcbb"))
print(long_sub("bbbbb"))  
print(long_sub("pwwkew"))                 

def most_water(nums):
     max_area = 0
     for i in range(len(nums)):
          for j in range(i+1, len(nums)):
               area = min(nums[i], nums[j]) * (j-i)  
               max_area = max( max_area , area)         
     return max_area

print(most_water([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(most_water([1, 1]))

def best_profit(prices):
     max_profit = 0
     for i in range(len(prices)):
          for j in range(i+1, len(prices)):
              # if prices [i] < prices [j]:
                    profit = prices[j] - prices[i]
                    max_profit = max(max_profit, profit)
     return max_profit
print(best_profit([7, 1, 5, 3, 6, 4]))
print(best_profit([7, 6, 4, 3, 1]))


#Find Maximum Number
def find_max(nums):
     max_num = 0
     for num in nums:
               if num > max_num:
                    max_num = num           
     return max_num

print(find_max([3, 1, 4, 1, 5, 9, 2, 6]))
print(find_max([10, 2, 5, 1]))

                    
#FizzBuzz
for num in range(1,21):
     if num % 3 == 0 and num % 5 == 0:
          print("FizzBuzz", end=" ")
     elif num % 3 == 0:
          print("Fizz", end=" ")
     elif num % 5 == 0: 
          print("Buzz", end=" ")
     else:
          print(num, end=" ")

#Reverse a String
def reverse(s):
    reversed_string = ""
    for i in range(len(s)-1, -1, -1):
        reversed_string += s[i]
    return reversed_string

print(reverse("hello"))   
print(reverse("python"))

#count_down
def count_down(num):
     while num != 0:
           print (num, end=" ")
           num -= 1
     print("Go!")      
       
count_down(10)

#Sum of digits
           