"""
====================================================================
 DecodeLabs - Python Programming Industrial Training Kit
 Project 3 : Random Password Generator
====================================================================

Goal
----
Ask the user for the desired password length and generate a
random, secure password using Python's built-in random and
string modules.

Concepts Used
-------------
1. Importing Modules
2. Functions
3. String Manipulation
4. Loops
5. Conditional Statements
6. Input Validation
7. Random Password Generation

Author : Laiba Maqbool
Batch  : 2026
====================================================================
"""

import random
import string

# ------------------------------------------------------------
# Configuration
# ------------------------------------------------------------

MIN_PASSWORD_LENGTH = 6
MAX_PASSWORD_LENGTH = 50

# Character Sets

LOWERCASE = string.ascii_lowercase
UPPERCASE = string.ascii_uppercase
DIGITS = string.digits
SYMBOLS = string.punctuation


# ------------------------------------------------------------
# Display Header
# ------------------------------------------------------------

def print_header():

    print("=" * 60)
    print("        RANDOM PASSWORD GENERATOR")
    print("      DecodeLabs Python Project 3")
    print("=" * 60)


# ------------------------------------------------------------
# Get Password Length
# ------------------------------------------------------------

def get_password_length():

    while True:

        user_input = input(
            f"\nEnter password length ({MIN_PASSWORD_LENGTH}-{MAX_PASSWORD_LENGTH}): "
        ).strip()

        if user_input.isdigit():

            length = int(user_input)

            if MIN_PASSWORD_LENGTH <= length <= MAX_PASSWORD_LENGTH:

                return length

            else:

                print(
                    f"Password length must be between "
                    f"{MIN_PASSWORD_LENGTH} and {MAX_PASSWORD_LENGTH}."
                )

        else:

            print("Please enter numbers only.")


# ------------------------------------------------------------
# User Preferences
# ------------------------------------------------------------

def ask_user_preferences():

    print("\nSelect character types for your password.\n")

    include_upper = input(
        "Include Uppercase Letters? (y/n): "
    ).lower() == "y"

    include_lower = input(
        "Include Lowercase Letters? (y/n): "
    ).lower() == "y"

    include_digits = input(
        "Include Numbers? (y/n): "
    ).lower() == "y"

    include_symbols = input(
        "Include Special Characters? (y/n): "
    ).lower() == "y"

    return (
        include_upper,
        include_lower,
        include_digits,
        include_symbols
    )


# ------------------------------------------------------------
# Build Character Pool
# ------------------------------------------------------------

def build_character_pool(
    upper,
    lower,
    digits,
    symbols
):

    pool = ""

    if upper:
        pool += UPPERCASE

    if lower:
        pool += LOWERCASE

    if digits:
        pool += DIGITS

    if symbols:
        pool += SYMBOLS

    return pool


# ------------------------------------------------------------
# Generate Password
# ------------------------------------------------------------

def generate_password(length, pool):

    password = ""

    for i in range(length):

        password += random.choice(pool)

    return password


# ------------------------------------------------------------
# Password Strength
# ------------------------------------------------------------

def check_strength(length):

    if length <= 7:

        return "Weak"

    elif length <= 11:

        return "Medium"

    elif length <= 15:

        return "Strong"

    else:

        return "Very Strong"
    # ------------------------------------------------------------
# Display Password
# ------------------------------------------------------------

def display_password(password, strength):

    print("\n" + "=" * 60)
    print("Generated Password")
    print("=" * 60)

    print(f"\nPassword : {password}")
    print(f"Length   : {len(password)}")
    print(f"Strength : {strength}")

    print("=" * 60)


# ------------------------------------------------------------
# Password History
# ------------------------------------------------------------

def show_history(history):

    print("\n" + "=" * 60)
    print("PASSWORD HISTORY")
    print("=" * 60)

    if len(history) == 0:

        print("No passwords generated.")

    else:

        for index, password in enumerate(history, start=1):

            print(f"{index}. {password}")

    print("=" * 60)


# ------------------------------------------------------------
# Main Function
# ------------------------------------------------------------

def main():

    history = []

    print_header()

    while True:

        length = get_password_length()

        (
            include_upper,
            include_lower,
            include_digits,
            include_symbols
        ) = ask_user_preferences()

        character_pool = build_character_pool(

            include_upper,
            include_lower,
            include_digits,
            include_symbols

        )

        if character_pool == "":

            print("\nYou must select at least one character type.")
            continue

        password = generate_password(

            length,
            character_pool

        )

        strength = check_strength(length)

        display_password(

            password,
            strength

        )

        history.append(password)

        choice = input(
            "\nGenerate another password? (y/n): "
        ).lower()

        if choice != "y":

            break

    show_history(history)

    print("\nThank you for using Random Password Generator.")
    print("Project Completed Successfully.")

    print("\nAuthor : Laiba Maqbool")


# ------------------------------------------------------------
# Program Entry Point
# ------------------------------------------------------------

if __name__ == "__main__":

    main()