#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")

greet_programmer()

def greet(name):
    print(f"Hello, {name}!")

greet("Naureen")


def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

# Call the function with no arguments
greet_with_default()

# Call the function with an argument
greet_with_default("Naureen")


def add(num1, num2):
    return num1 + num2
# Call the function with two arguments and print the result
sum_value = add(1, 2)
print(sum_value)


def halve(number):
    if not isinstance(number, (int, float)):
        return None

    return number / 2

# Test cases
result1 = halve(4)
print(result1)  # Output: 2.0

result2 = halve("two")
print(result2)  # Output: None

