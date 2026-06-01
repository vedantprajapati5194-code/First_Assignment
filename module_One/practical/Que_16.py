''' Q:4)  Practical Example 4: Print this pattern using nested for loop:
markdown
Copy code
*
**
***
****
*****
'''

# Print star pattern

for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()