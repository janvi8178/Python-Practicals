# Name: Janvi
# Roll Number: 26570025

# Practical 10: Write a function that prints a dictionary where the keys are numbers
# between 1 and 5 and the values are cubes of the keys.


def print_cubes_dict():
    cubes = {}
    for n in range(1, 6):
        cubes[n] = n ** 3
    print(cubes)
    return cubes


print_cubes_dict()
