''' Q:4)  Practical Example 8: Write a Python program to check if a person is eligible to donate blood
using a nested if.'''

# Enter age and weight

age = int(input("Enter your age: "))
weight = int(input("Enter your weight: "))

# Check eligibility

if age >= 18:
    if weight >= 50:
        print("Eligible to donate blood")
    else:
        print("Not eligible (Weight is less than 50 kg)")
else:
    print("Not eligible (Age is less than 18)")