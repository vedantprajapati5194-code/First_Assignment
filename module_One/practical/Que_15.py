''' Q:3)  Practical Example 3: Write a Python program to find a specific string in the list using a simple
for loop and if condition.'''

# Create a list

list1 = ['apple', 'banana', 'mango']

# String to search

search = "banana"

# Check each item in the list

for fruit in list1:
    if fruit == search:
        print("Found:", fruit)