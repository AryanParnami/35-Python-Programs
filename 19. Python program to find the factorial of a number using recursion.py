def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

# Example usage
num = int(input("Enter a number to find its factorial: "))
result = factorial_recursive(num)
print(f"The factorial of {num} is {result}.")
