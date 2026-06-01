## 10. Advanced Python (map(), reduce(), filter(), Closures and Decorators)


## Q:1) Write a Python program to apply the map() function to square a list of numbers.

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Function to square a number
def square(n):
    return n * n

# Apply map() to square each number
result = map(square, numbers)

# Convert result to list and print
print(list(result))