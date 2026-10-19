# Name: Janvi
# Roll Number: 26570025

# Practical 3: WAP to create a pyramid of the character '*' and a reverse pyramid


def pyramid(rows):
    """Print a pyramid with the given number of rows (1, 3, 5, ... stars)."""
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "*" * (2 * i - 1))


def reverse_pyramid(rows):
    """Print a reverse (inverted) pyramid with the given number of rows."""
    for i in range(rows, 0, -1):
        print(" " * (rows - i) + "*" * (2 * i - 1))


rows = int(input("Enter the number of rows: "))

print("\nPyramid:\n")
pyramid(rows)

print("\nReverse pyramid:\n")
reverse_pyramid(rows)
