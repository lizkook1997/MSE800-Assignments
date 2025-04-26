# class Factorial:
#     def find(self, n):
#         result = 1
#         for i in range(2, n + 1):
#             result *= i
#         return result


# f = Factorial()

# for num in range(5):
#     print(f"Factorial of {num} is {f.find(num)}")

class Factorial:
    def find(self, n):
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

    def is_prime(self, n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True


f = Factorial()

# Input from the user
num = int(input("Enter a number: "))

# Check if prime or not and calculate factorial
if f.is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")

print(f"Factorial of {num} is {f.find(num)}")

