from math import prod

def factorial(n):
    return prod(range(1, n + 1))

# Count from 1 to 4 and print factorial of each
for num in range(5):
    print(factorial(num))