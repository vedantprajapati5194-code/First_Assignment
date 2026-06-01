## Q:2)  Practical Example 6: Write a Python program to check if a number is prime using if_else

# Check if a number is prime

num = int(input("Enter a number: "))

if num == 2:
    print("Prime Number")
elif num % 2 == 0:
    print("Not a Prime Number")
else:
    print("Prime Number")