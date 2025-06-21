import random
import string

# Generate password
chars = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(chars) for _ in range(8))

print("Generated Password:", password)