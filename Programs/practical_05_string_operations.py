# Name: Janvi
# Roll Number: 26570025

# Practical 5: WAP to perform the following operations on a string
#   a. Find the frequency of a character in a string
#   b. Replace a character by another character in a string
#   c. Remove the first occurrence of a character from a string
#   d. Remove all occurrences of a character from a string


def frequency(s, ch):
    count = 0
    for c in s:
        if c == ch:
            count += 1
    return count


def replace_char(s, old, new):
    result = ""
    for c in s:
        result += new if c == old else c
    return result


def remove_first(s, ch):
    index = s.find(ch)
    if index == -1:
        return s
    return s[:index] + s[index + 1:]


def remove_all(s, ch):
    result = ""
    for c in s:
        if c != ch:
            result += c
    return result


text = input("Enter a string: ")

ch = input("a) Enter a character to find its frequency: ")[:1]
print(f"   '{ch}' occurs {frequency(text, ch)} time(s)")

old = input("b) Enter the character to be replaced: ")[:1]
new = input("   Enter the new character: ")[:1]
print("   Result:", replace_char(text, old, new))

ch = input("c) Enter a character to remove its first occurrence: ")[:1]
print("   Result:", remove_first(text, ch))

ch = input("d) Enter a character to remove all its occurrences: ")[:1]
print("   Result:", remove_all(text, ch))
