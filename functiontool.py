from functools import partial

# https://t.me/LearnPython3

def multiply(x, y):
    return x * y

# Create a new function where y is always 2
double = partial(multiply, y=2)

print(double(5))  # Output: 10