import random

def generate_password(length):
    if length < 4:
        return "Password length should be at least 4"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    digits = "0123456789"
    symbols = "!@#$%^&*()-_=+[]{}|;:,.<>?/"

    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(symbols)
    ]

    all_chars = uppercase + lowercase + digits + symbols

    password += [random.choice(all_chars) for _ in range(length - 4)]

    random.shuffle(password)

    return ''.join(password)

print("Your random password is:", generate_password(16))
