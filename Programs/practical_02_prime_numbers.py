# Name: Janvi
# Roll Number: 26570025

# Practical 2: WAP to accept a number 'n' and
#   a. Check if 'n' is prime
#   b. Generate all prime numbers till 'n'
#   c. Generate first 'n' prime numbers
# (done using functions)


def is_prime(num):
    """Return True if num is a prime number."""
    if num < 2:
        return False
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True


def primes_till(n):
    """Return a list of all primes <= n."""
    return [i for i in range(2, n + 1) if is_prime(i)]


def first_n_primes(n):
    """Return a list of the first n primes."""
    result = []
    candidate = 2
    while len(result) < n:
        if is_prime(candidate):
            result.append(candidate)
        candidate += 1
    return result


n = int(input("Enter a number n: "))

# a
if is_prime(n):
    print(f"a) {n} is a prime number")
else:
    print(f"a) {n} is not a prime number")

# b
print(f"b) Prime numbers till {n}:", primes_till(n))

# c
print(f"c) First {n} prime numbers:", first_n_primes(n))
