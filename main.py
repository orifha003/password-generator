import random
import string

def generate_password(min_Length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    
    characters = letters 
    if numbers:
        characters += digits
    if special_characters:
        characters+=special

    pwd=""
    meet_criteria = False
    has_number = False
    has_special = False

    while not meet_criteria or len(pwd) < min_Length:
        new_char = random.choice (characters)
        pwd += new_char

        if new_char in digits: 
            has_number = True
        elif new_char in special:
            has_special = True
        meet_criteria = (
            len(pwd) >= min_length
            and (not numbers or has_number)
            and (not special_characters or has_special)
        )

    return pwd


if __name__ == "__main__":
    password = generate_password(12)
    print(password)