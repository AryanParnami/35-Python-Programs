def fibonacci_iteration(n):
    fib_series = [0, 1]
    for i in range(2, n):
        next_term = fib_series[i - 1] + fib_series[i - 2]
        fib_series.append(next_term)
    return fib_series

# Example usage
terms = int(input("Enter the number of terms in the Fibonacci series: "))
result = fibonacci_iteration(terms)
print(f"The Fibonacci series is: {result}")
