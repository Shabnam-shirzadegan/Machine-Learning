# ---- Exercise 1: List comprehension - squares ----
def squares(nums):
   return [num**2 for num in nums]

# ---- Exercise 2: List comprehension - filter words by length ----
def long_words(l):
    return [word for word in l if len(word) > 4]





if __name__ == "__main__":
    print("Exercise1_output:", squares([1, 2, 3, 4, 5]))
    print("Exercise2_output:", long_words(["cat", "elephant", "dog", "python", "hi"]))
