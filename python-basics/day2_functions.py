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




if __name__ == "__main__":
    print("Exercise1_output:", squares([1, 2, 3, 4, 5]))
    print("Exercise2_output:", long_words(["cat", "elephant", "dog", "python", "hi"]))
    print("Exercise3_output:", c_to_f([0, 20, 37, 100]))
    print("Exercise4_output:", flatter([[1, 2], [3, 4], [5, 6]]))
    print("Exercise5_output:", dict_maker(["name", "age", "city"], ["Shabnam", 36, "Vancouver"]))