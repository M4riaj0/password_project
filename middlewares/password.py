import random
import string

def password_generator(requirements: dict):
    password = ""
    character_types = ""
    if requirements.mayus:
        character_types += string.ascii_uppercase
    if requirements.minus:
        character_types += string.ascii_lowercase
    if requirements.numbers:
        character_types += string.digits
    if requirements.symbols:
        character_types += string.punctuation
    character_types = ''.join(random.sample(character_types, len(character_types)))
    if character_types == "":
        return None
    while requirements.length > 0:
        password += random.choice(character_types)
        requirements.length -= 1
    return password