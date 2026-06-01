''' Q:2) Practical Example: 2) Write a Python program to stop the loop once 'banana' is found using
the break statement.'''

# Create a list
list1 = ['apple', 'banana', 'mango']

# Loop through the list
for fruit in list1:
    if fruit == "banana":
        break  # stop loop when banana is found
    print(fruit)