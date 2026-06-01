## 8. Control Statements (Break, Continue, Pass)


'''Q:1) Practical Example: 1) Write a Python program to skip 'banana' in a list using the continue
statement. List1 = ['apple', 'banana', 'mango']'''

# Create a list
list1 = ['apple', 'banana', 'mango']

# Loop through the list
for fruit in list1:
    if fruit == "banana":
        continue  # skip banana
    print(fruit)