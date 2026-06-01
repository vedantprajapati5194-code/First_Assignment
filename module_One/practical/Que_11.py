''' Q:3)  Practical Example 7: Write a Python program to calculate grades based on percentage using
if-else ladder'''

# Enter percentage

percentage = float(input("Enter your percentage: "))

# Check grade

if percentage >= 90:
    print("Grade A")
elif percentage >= 75:
    print("Grade B")
elif percentage >= 60:
    print("Grade C")
elif percentage >= 40:
    print("Grade D")
else:
    print("Fail")