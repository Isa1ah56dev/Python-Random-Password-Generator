import random
import string

def generate_password(length, all_chars):
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

def main():
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    symbols = string.punctuation

    include_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    include_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
    include_digits = input("Include numbers? (y/n): ").lower() == 'y'
    include_symbols = input("Include special characters? (y/n): ").lower() == 'y'

    all_chars = ""
    if include_upper:
        all_chars += uppercase
    if include_lower:
        all_chars += lowercase
    if include_digits:
        all_chars += digits
    if include_symbols:
        all_chars += symbols

    if not all_chars:
        print("Error: At least one character type must be selected.")
        return

    try:
        length_input = input("Enter password length: ")

        length = int(length_input)
        if length <= 0:
            print("Invalid input. Password length must be a positive integer.")
            return

        password = generate_password(length, all_chars)
        print(f"Generated password: {password}")

        input("Press Enter to exit...")

    except ValueError:
        print("Invalid input. Please enter a valid integer for password length.")

if __name__ == "__main__":
    main()