def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Count from 1 to 4 and print factorial of each
for num in range(0, 5):
    print(f"Factorial of {num} is {factorial(num)}")