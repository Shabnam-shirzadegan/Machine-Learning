def write_word(filename, word):
    with open(filename, "w") as f:
        f.write("Hello\n")
        f.write("World")

def write_lines(filename, lines):
    with open(filename, "w") as f:
        for line in lines:
            f.write(line + "\n")


# ---- Exercise 2: File I/O - read a file and return its lines as a list ----
def read_lines(filename):
    with open(filename, "r") as f:
         lines = f.readlines()
         result = []
         for line in lines:
             result.append(line.strip())
         return result


# ---- Exercise 3: File I/O - append a line to an existing file ----
def append_line(filename, line):
    with open(filename, "a") as f:
        f.write(line + "\n")

# ---- Exercise 4: File I/O - count words in a file ----
def count_words(filename):
    counter = 0
    with open(filename, "r") as f:
        for line in f:
            words = line.split()
            counter += len(words)
        return counter 

if __name__ == "__main__":
    write_word("output0.txt", "Hello")
    write_lines("output.txt", ["hello", "world", "python"])
    print(read_lines("output.txt"))
    append_line("output.txt", "new line")
    print(read_lines("output.txt"))
    print("Word count:", count_words("output.txt"))
    print(read_lines("missing.txt"))
