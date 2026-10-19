# Name: Janvi
# Roll Number: 26570025

# Practical 15: WAP to accept a name from a user. Raise and handle appropriate
# exception(s) if the text entered by the user contains digits and/or special characters.


class InvalidNameError(Exception):
    """Raised when the name has digits or special characters."""
    pass


def validate_name(name):
    if name.strip() == "":
        raise ValueError("Name cannot be empty.")
    has_digit = any(ch.isdigit() for ch in name)
    has_special = any(not (ch.isalpha() or ch.isspace()) and not ch.isdigit() for ch in name)
    if has_digit and has_special:
        raise InvalidNameError("Name contains digits and special characters.")
    if has_digit:
        raise InvalidNameError("Name contains digits.")
    if has_special:
        raise InvalidNameError("Name contains special characters.")
    return name


while True:
    user_name = input("Enter your name: ")
    try:
        validate_name(user_name)
    except InvalidNameError as e:
        print("Invalid name ->", e, "Please try again.\n")
    except ValueError as e:
        print("Error ->", e, "Please try again.\n")
    else:
        print("Hello,", user_name.strip() + "! Your name is valid.")
        break
    finally:
        print("(validation finished)")
