## Q:2)  Write a Python program that uses a custom iterator to iterate over a list of integers.

# Custom iterator for a list of integers

class MyNumbers:
    def __init__(self, numbers):
        self.numbers = numbers
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.numbers):
            value = self.numbers[self.index]
            self.index += 1
            return value
        else:
            raise StopIteration


# Create a list of integers
num_list = [10, 20, 30, 40, 50]

# Create iterator object
my_iter = MyNumbers(num_list)

# Use iterator
for num in my_iter:
    print(num)