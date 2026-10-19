# Name: Janvi
# Roll Number: 26570025

# Practical 9: WAP to read a file and
#   a. Print the total number of characters, words and lines in the file.
#   b. Calculate the frequency of each character in the file. Use a variable of
#      dictionary type to maintain the count.
#   c. Print the words in reverse order.
#   d. Copy even lines of the file to a file named 'File1' and odd lines to another
#      file named 'File2'.
import os

filename = input("Enter the file name (press Enter to use sample.txt): ").strip() or "sample.txt"

# Create a sample file if the default one does not exist yet
if filename == "sample.txt" and not os.path.exists(filename):
    with open(filename, "w") as f:
        f.write("Python is a popular programming language.\n"
                "It is easy to learn and read.\n"
                "File handling is an important topic.\n"
                "This is the fourth line of the file.\n"
                "And this is the last line.\n")
    print("(sample.txt created)")

try:
    with open(filename, "r") as f:
        lines = f.readlines()
except FileNotFoundError:
    print("File not found:", filename)
    raise SystemExit

content = "".join(lines)

# a. characters, words, lines
print("\na) Total characters:", len(content))
print("   Total words     :", len(content.split()))
print("   Total lines     :", len(lines))

# b. frequency of each character (dictionary)
freq = {}
for ch in content:
    freq[ch] = freq.get(ch, 0) + 1
print("\nb) Frequency of each character:")
for ch, count in sorted(freq.items()):
    print(f"   {repr(ch):6} -> {count}")

# c. words in reverse order
print("\nc) Words in reverse order:")
print("  ", " ".join(content.split()[::-1]))

# d. even lines -> File1, odd lines -> File2  (line numbers start from 1)
with open("File1", "w") as f1, open("File2", "w") as f2:
    for number, line in enumerate(lines, start=1):
        if number % 2 == 0:
            f1.write(line if line.endswith("\n") else line + "\n")
        else:
            f2.write(line if line.endswith("\n") else line + "\n")
print("\nd) Even lines copied to 'File1' and odd lines copied to 'File2'.")
