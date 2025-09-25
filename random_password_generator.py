# collect user preferences, length, uppercase, lowercase, numbers, special characters

import random

length = input("Enter the length of the password: ")
uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
numbers = input("Include numbers? (y/n): ").lower() == 'y'
special = input("Include special characters? (y/n): ").lower() == 'y'
length = int(length)
if length < 8 or length > 128:
    print("Password length must be between 8 and 128 characters.")
    exit()
if not (uppercase or lowercase or numbers or special):
    print("At least one character type must be selected.")
    exit()
char_pool = ""
password_chars = []
if uppercase:
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    char_pool += chars
    password_chars.append(random.choice(chars))
if lowercase:
    chars = "abcdefghijklmnopqrstuvwxyz"
    char_pool += chars
    password_chars.append(random.choice(chars))
if numbers:
    chars = "0123456789"
    char_pool += chars
    password_chars.append(random.choice(chars))
if special:
    chars = "!@#$%^&*()-_=+[]{}|;:',.<>?/`~"
    char_pool += chars
    password_chars.append(random.choice(chars))

remaining = length - len(password_chars)
password_chars.extend(random.choice(char_pool) for _ in range(remaining))
random.shuffle(password_chars)
password = ''.join(password_chars)
print(f"Generated password: {password}")
