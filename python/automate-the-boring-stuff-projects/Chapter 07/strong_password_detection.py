"""Detects if the user's password is strong"""

# TODO: check if password is at least eight characters long

# TODO: check if password contains both uppercase and lowercase characters

# TODO: check if password contains at least one digit

import re, getpass

length_checker = re.compile(r".{8,}")  # >= 8 characters
upper_case_checker = re.compile(r"[A-Z]")  # Contains a upper case letter
lower_case_checker = re.compile(r"[a-z]")  # Contains a lower case letter
digit_checker = re.compile(r"\d")  # Contains a digit


def password_checker(password):
    if length_checker.search(password) == None:
        return False
    if upper_case_checker.search(password) == None:
        return False
    if lower_case_checker.search(password) == None:
        return False
    if digit_checker.search(password) == None:
        return False
    else:
        return True


print("Enter your password to check if it is secure")
password = getpass.getpass()
print("Password is secure:")
print(password_checker(password))
