def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Example usage
term = int(input("Enter the value of N: "))
result = fibonacci_recursive(term)
print(f"The {term}th term in the Fibonacci series is: {result}")
