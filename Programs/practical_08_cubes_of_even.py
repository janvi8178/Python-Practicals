# Name: Janvi
# Roll Number: 26570025

# Practical 8: WAP to create a list of the cubes of only the even integers appearing
# in the input list (may have elements of other types also) using:
#   a. 'for' loop
#   b. list comprehension

# The input list is mixed on purpose: ints, floats, strings, bool and None.
data = [1, 2, 3, 4, "hello", 6, 7.0, 8, 9, 10, True, None, "12", 14, -2]
print("Input list:", data)


def is_integer(x):
    # bool is a subclass of int in Python, so it is excluded explicitly
    return isinstance(x, int) and not isinstance(x, bool)


# a. using a for loop
cubes_loop = []
for item in data:
    if is_integer(item) and item % 2 == 0:
        cubes_loop.append(item ** 3)
print("a) Using for loop          :", cubes_loop)

# b. using list comprehension
cubes_comp = [x ** 3 for x in data if is_integer(x) and x % 2 == 0]
print("b) Using list comprehension:", cubes_comp)
