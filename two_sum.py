def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]
            
print(two_sum([2,7,2,4],9))

#hasmaps

def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        needed = target - num
        if needed in seen:
            return [seen[needed],i]
        seen[num]=i


def dublicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
print (dublicate([1,2,3,1]))
print(dublicate([1, 2, 3, 4])) 
print(dublicate([1, 1, 1, 3])) 



def is_anagram(s, t):
    if len(t) != len(s):
        return False
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1
    for char in t:
        count[char] = count.get(char, 0) - 1
    for val in count.values():
            if val != 0:
                return False
    return True

print(is_anagram("rat", "tar"))     # True
print(is_anagram("rat", "car"))     # False
print(is_anagram("listen", "silent"))  # True


def is_palindrome(my_string):
    my_string = my_string.lower()
    my_string = ''.join(char for char in my_string if char.isalnum())
    if my_string == my_string[::-1]:
        return True
    return False 

print(is_palindrome("racecar"))                      # True
print(is_palindrome("hello"))                        # False
print(is_palindrome("A man a plan a canal Panama"))  # True




def length_of_longest_substring(s):
    seen = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        max_length = max(max_length, right - left + 1)
    return max_length
print(length_of_longest_substring("abcabcbb"))  # 3
print(length_of_longest_substring("bbbbb"))     # 1
print(length_of_longest_substring("pwwkew"))    # 3


def duplicate(my_string):
    end = 0 
    max = 0
    seen = set()

    for start in range(len(my_string)):
        while my_string[start] in seen:
            seen.remove(my_string[end])
            end += 1
        seen.add(my_string[start])
        max_length = max(max_length, right - left + 1)
    return max_length
print(length_of_longest_substring("abcabcbb"))  # 3
print(length_of_longest_substring("bbbbb"))     # 1
print(length_of_longest_substring("pwwkew"))    # 3


def max_water(heights):
    left = 0
    right = len(heights) - 1
    max_area = 0
    while left < right:
        area = min(heights[left], heights[right]) * (right - left)
        max_area = max(max_area, area)
        if heights[left] < heights[right]:
            left += 1
        else:
         right -=1
    return max_area
print(max_water([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # 49
print(max_water([1, 1]))                          # 1




def three_sum(nums):
    nums.sort()
    result=[]
    
    for i in range(len(nums)):
        if i >0 and nums[i] - nums [i-1] == 0:
            continue
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
              if  nums[i] + nums[j] + nums[k] == 0: 
                  result.append([nums[i] , nums[j] , nums[k]])
    return result  

print(three_sum([-1, 0, 1, 2, -1, -4]))
# should be [[-1, 0, 1], [-1, -1, 2]]


























































































                                                                                    