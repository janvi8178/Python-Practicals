# Name: Janvi
# Roll Number: 26570025

# Practical 6: WAP to swap the first n characters of two strings


def swap_first_n(s1, s2, n):
    """Return (s1', s2') after exchanging the first n characters."""
    return s2[:n] + s1[n:], s1[:n] + s2[n:]


str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
n = int(input("Enter n (number of characters to swap): "))

if n < 0 or n > len(str1) or n > len(str2):
    print("n must be between 0 and the length of the shorter string.")
else:
    new1, new2 = swap_first_n(str1, str2, n)
    print("Before swapping:", str1, "|", str2)
    print("After swapping :", new1, "|", new2)
