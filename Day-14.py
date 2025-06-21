def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)

num = int(input("Enter a non-negative integer: "))

print(f"The factorial of {num} is {factorial(num)}")