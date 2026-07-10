# ---- Exercise 1: File I/O - write a list of lines to a file ----
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


if __name__ == "__main__":
    write_lines("output.txt", ["hello", "world", "python"])
    print(read_lines("output.txt"))
