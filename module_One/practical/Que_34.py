## Q:3) Write a Python program that filters out even numbers using the filter() function.

# List of numbers
numbers = [10, 15, 20, 25, 30, 35, 40]

# Function to check even number
def is_even(n):
    return n % 2 == 0

# Use filter() to get even numbers
even_numbers = filter(is_even, numbers)

# Convert result to list and print
print("Even numbers:", list(even_numbers))
