import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def power(a, b):
    return a ** b

def square_root(a):
    if a < 0:
        raise ValueError("Cannot calculate square root of a negative number")
    return math.sqrt(a)

# Memory operations
_memory = 0

def memory_store(value):
    global _memory
    _memory = value
    return value

def memory_recall():
    return _memory

def memory_clear():
    global _memory
    _memory = 0
    return 0

def memory_add(value):
    global _memory
    _memory += value
    return _memory