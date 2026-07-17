import csv 
print("CSV imported successfully")
import json

def write_word(filename):
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

# ---- Exercise 5: Exceptions - safely read a file ----
def safe_read_lines(filename):
    try:
        return read_lines(filename)
    except FileNotFoundError:
        print("The file was not found.")
        return []

# ---- Exercise 6: CSV - read data from a CSV file ----
def write_csv_file(filename):
    with open(filename, "w") as f:
        f.write("location,bacteria_count\n")
        f.write("River,12\n")
        f.write("Lake,25\n")
        f.write("Beach,8")

# ---- Exercise 7: CSV - read rows from a CSV file ----
def read_csv_file(filename):
    with open(filename, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

# ---- Exercise 8: JSON - write data to a JSON file ----
def write_json(filename, data):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

    





if __name__ == "__main__":
    write_word("output0.txt")
    write_lines("output.txt", ["hello", "world", "python"])
    print(read_lines("output.txt"))
    append_line("output.txt", "new line")
    print(read_lines("output.txt"))
    print("Word count:", count_words("output.txt"))
    print(safe_read_lines("missing.txt"))
    write_csv_file("water_data.csv")
    read_csv_file("water_data.csv")
    water_sample = {
    "location": "River",
    "bacteria_count": 12
    }
    write_json("water_sample.json", water_sample)

    
