# Name: Janvi
# Roll Number: 26570025

# Practical 4: WAP that accepts a character and performs the following:
#   a. print whether the character is a letter or numeric digit or a special character
#   b. if the character is a letter, print whether the letter is uppercase or lowercase
#   c. if the character is a numeric digit, print its name in text (e.g. 9 -> NINE)

DIGIT_NAMES = {
    '0': "ZERO", '1': "ONE", '2': "TWO", '3': "THREE", '4': "FOUR",
    '5': "FIVE", '6': "SIX", '7': "SEVEN", '8': "EIGHT", '9': "NINE",
}

ch = input("Enter a single character: ")

if len(ch) != 1:
    print("Please enter exactly one character.")
elif ch.isalpha():
    print(f"'{ch}' is a letter")
    if ch.isupper():
        print("It is an uppercase letter")
    else:
        print("It is a lowercase letter")
elif ch.isdigit():
    print(f"'{ch}' is a numeric digit")
    print("Name in text:", DIGIT_NAMES.get(ch, "(not a decimal digit 0-9)"))
else:
    print(f"'{ch}' is a special character")
