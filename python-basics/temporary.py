def squares(nums):
    return [item**2 for item in nums]

def long_words(nums):
    return [words for words in nums if len(words)>4]
    
def c_to_f(nums):
    return [C * 9/5 + 32 for C in nums]

def flatter(nums):
    return [item for sublist in nums for item in sublist]

def dict_maker(keys,values):
    return {key: value for key, value in zip(keys, values)}

def word_lengths(words):
    return {word: len(word) for word in words}

def no_vomwels(word):
    vowels = "aeiou"
    return "".join(letter for letter in word if letter not in vowels)

def multiplication_table(n):
    return [ for range(n)]







if __name__ == "__main__":
    print("Exercise1_output:", squares([1, 2, 3, 4, 5]))
    print("Exercise2_output:", long_words(["cat", "elephant", "dog", "python", "hi"]))
    print("Exercise3_output:", c_to_f([0, 20, 37, 100]))
    print("Exercise4_output:", flatter([[1, 2], [3, 4], [5, 6]]))
    print("Exercise5_output:", dict_maker(["name", "age", "city"], ["Shabnam", 36, "Vancouver"]))
    print("Exercise6_output:", word_lengths(["hello", "world", "python"]))
    print("Exercise7_output:", no_vomwels("hello world"))
    print("Exercise8_output:", multiplication_table(3))
   # print("Exercise9_output:", common_elements([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))
   # print("Exercise10_output:", vowels(["hello", "world", "python"]))
   # print("Exercise11_output:", square_even_numbers([1, 2, 3, 4, 5, 6]))
   # print("Exercise12_output:", replace([3, -1, 4, -1, 5, -9, 2, -6]))
   # print("Exercise13_output:", uppercase(["apple", "banana", "orange", "grape"]))
   # print("Exercise14_output:", pair_lists([1, 2, 3], ["a", "b", "c"]))
   # print("Exercise15_output:", group_numbers([1, 2, 3, 4, 5, 6]))
   # print("Exercise16_output:", transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))