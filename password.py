import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Example usage
password_length = int(input("Enter the length of the password: "))
print(f"Generated password: {generate_password(password_length)}")
