import random
import string

def generate_password(length = 12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.SystemRandom().choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    length = int(input("Enter password length (default 12) : ") or 12)
    password = generate_password(length)
    print(f"\nGenerated Password : {password}")
