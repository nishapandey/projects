# collect user preferences, length, uppercase, lowercase, numbers, special characters

import random

len = input("Enter the length of the password: ")
uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
numbers = input("Include numbers? (y/n): ").lower() == 'y'
special = input("Include special characters? (y/n): ").lower() == 'y'
len = int(len)
if len < 8 or len > 128:
    print("Password length must be between 8 and 128 characters.")
    exit()
if not (uppercase or lowercase or numbers or special):
    print("At least one character type must be selected.")
    exit()
char_pool = ""
if uppercase:
    char_pool += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
if lowercase:
    char_pool += "abcdefghijklmnopqrstuvwxyz"
if numbers:
    char_pool += "0123456789"
if special:
    char_pool += "!@#$%^&*()-_=+[]{}|;:',.<>?/`~"
password = ''.join(random.choice(char_pool) for _ in range(len))
print(f"Generated password: {password}")
