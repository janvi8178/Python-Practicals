# Name: Janvi
# Roll Number: 26570025

# Practical 7: Write a function that accepts two strings and returns the indices of
# all the occurrences of the second string in the first string as a list.
# If the second string is not present in the first string then it should return -1.


def find_all(first, second):
    indices = []
    start = first.find(second)
    while start != -1:
        indices.append(start)
        start = first.find(second, start + 1)   # +1 also finds overlapping matches
    return indices if indices else -1


s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")

if s2 == "":
    print("The second string must not be empty.")
else:
    print("Result:", find_all(s1, s2))
