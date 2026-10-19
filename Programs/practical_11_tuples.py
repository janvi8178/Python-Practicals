# Name: Janvi
# Roll Number: 26570025

# Practical 11: Consider a tuple t1 = (1, 2, 5, 7, 9, 2, 4, 6, 8, 10).
# WAP to perform following operations:
#   a) Print half the values of the tuple in one line and the other half in the next line
#   b) Print another tuple whose values are even numbers in the given tuple
#   c) Concatenate a tuple t2 = (11, 13, 15) with t1
#   d) Return maximum and minimum value from this tuple

t1 = (1, 2, 5, 7, 9, 2, 4, 6, 8, 10)
print("t1 =", t1)

# a) first half on one line, second half on the next
mid = len(t1) // 2
print("\na) First half :", *t1[:mid])
print("   Second half:", *t1[mid:])

# b) tuple of even numbers
evens = tuple(x for x in t1 if x % 2 == 0)
print("\nb) Even numbers tuple:", evens)

# c) concatenation with t2
t2 = (11, 13, 15)
t3 = t2 + t1
print("\nc) t2 + t1 =", t3)


# d) maximum and minimum
def max_min(t):
    return max(t), min(t)


maximum, minimum = max_min(t1)
print("\nd) Maximum value:", maximum)
print("   Minimum value:", minimum)
