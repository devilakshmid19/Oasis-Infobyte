import random
import string

def password_generator(length, include_letter=True, include_number = True, include_symbol = True):
    ch = ''
    if include_letter:
        ch += string.ascii_letters
    if include_number:
        ch +=string.digits
    if include_symbol:
        ch += string.punctuation
    if not ch:
        print("Error: Please include at least one character type.")
        return None
    return ''.join(random.choice(ch) for _ in range(length))

def main():
    len = int(input("Enter the length of your password:"))
    include_letter = input("Include letters (y/n): ").lower() == 'y'
    include_number = input("Include numbers (y/n):").lower() == 'y'
    include_symbol = input("Include symbols (y/n):").lower() == 'y'
    password = password_generator(len, include_letter, include_number, include_symbol)
    if password:
        print("Generated password:",password)

if __name__ == "__main__":
    main()