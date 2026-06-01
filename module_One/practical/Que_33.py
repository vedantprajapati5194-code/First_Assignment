## Q:2)  Write a Python program that uses reduce() to find the product of a list of numbers.

from functools import reduce

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Function to multiply two numbers
def multiply(a, b):
    return a * b

# Apply reduce to find product
result = reduce(multiply, numbers)

# Print result
print("Product of list:", result)