# ---- Exercise 1: List comprehension - squares ----
def squares(nums):
   return [num**2 for num in nums]

# ---- Exercise 2: List comprehension - filter words by length ----
def long_words(l):
    return [word for word in l if len(word) > 4]

# ---- Exercise 3: List comprehension - convert Celsius to Fahrenheit ----
def c_to_f(num):
    return [C * 9/5 + 32 for C in num]

# ---- Exercise 4: List comprehension - flatten a nested list ----
def flatter(l):
    return [item for sublist in l for item in sublist]

# ---- Exercise 5: List comprehension - dictionary from two lists ----
def dict_maker(keys, values):
    return {key: value for key, value in zip(keys, values)}

# ---- Exercise 6: List comprehension - word lengths ----
def word_lengths(l):
    return {word: len(word) for word in l}

# ---- Exercise 7: List comprehension - remove vowels from a string ----
def no_vomwels(s):
    vowels = "aeiou"
    return "".join(letter for letter in s if letter not in vowels)

# ---- Exercise 8: List comprehension - nested multiplication table ----
def multiplication_table(n):
    return [[i * j for j in range(1, n+1)] for i in range(1, n+1)]
    
# ---- Exercise 9: List comprehension - find common elements using comprehension ----
def common_elements(l1, l2):
    return [i for i in l1 if i in l2]

# ---- Exercise 10: List comprehension - count vowels in each word ----
def vowels(l):
    vowels="aeiou"
    return {key: sum(1 for letter in key if letter in vowels) for key in l}

# ---- Exercise 11: List comprehension - square of even numbers only ----
def square_even_numbers(nums):
    return [num**2 for num in nums if num % 2 == 0]

# ---- Exercise 12: List comprehension - replace negative numbers with zero ----
def replace(nums):
    return [0 if num < 0 else num for num in nums]

# ---- Exercise 13: List comprehension - uppercase words that start with a vowel ----
def uppercase(l):
    vowels = "aeiou"
    return [word.upper() if word[0] in vowels else word for word in l ]
    
# ---- Exercise 14: List comprehension - zip two lists into pairs ----
def pair_lists (l1, l2):
    return list (zip(l1, l2))

# ---- Exercise 15: List comprehension - group numbers as even or odd ----
def group_numbers(nums):
    dict =  {"even": [], "odd": []}
    for num in nums:
        if num % 2 == 0:
            dict["even"].append(num)
        else:
            dict["odd"].append(num)
    return dict



if __name__ == "__main__":
    print("Exercise1_output:", squares([1, 2, 3, 4, 5]))
    print("Exercise2_output:", long_words(["cat", "elephant", "dog", "python", "hi"]))
    print("Exercise3_output:", c_to_f([0, 20, 37, 100]))
    print("Exercise4_output:", flatter([[1, 2], [3, 4], [5, 6]]))
    print("Exercise5_output:", dict_maker(["name", "age", "city"], ["Shabnam", 36, "Vancouver"]))
    print("Exercise6_output:", word_lengths(["hello", "world", "python"]))
    print("Exercise7_output:", no_vomwels("hello world"))
    print("Exercise8_output:", multiplication_table(3))
    print("Exercise9_output:", common_elements([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))
    print("Exercise10_output:", vowels(["hello", "world", "python"]))
    print("Exercise11_output:", square_even_numbers([1, 2, 3, 4, 5, 6]))
    print("Exercise12_output:", replace([3, -1, 4, -1, 5, -9, 2, -6]))
    print("Exercise13_output:", uppercase(["apple", "banana", "orange", "grape"]))
    print("Exercise14_output:", pair_lists([1, 2, 3], ["a", "b", "c"]))
    print("Exercise15_output:", group_numbers([1, 2, 3, 4, 5, 6]))


