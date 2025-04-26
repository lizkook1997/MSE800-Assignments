class Factorial:
    def find(self, n):
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result


f = Factorial()

for num in range(5):
    print(f"Factorial of {num} is {f.find(num)}")
