import random

def plus(a = 1, b = 1):
    return (a + b)
def minus(a = 1, b = 1):
    return (a - b)
def multiply(a = 1, b = 1):
    return (a * b)
def divide(a = 1, b = 1):
    return (a / b)

a = random.randint(1, 100)
b = random.randint(1, 100)

print("a=",a, "b=",b, "\n")

print(plus(a, b))
print(minus(a, b))
print(multiply(a, b))
print(divide(a, b), "\n")

print(plus())
print(minus())
print(multiply())
print(divide())