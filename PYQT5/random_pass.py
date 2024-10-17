import random


def randChar(chars):
    return random.choice(chars)


def randomPass(chars, passLen):
    password = "".join(randChar(chars) for _ in range(passLen))
    return password
