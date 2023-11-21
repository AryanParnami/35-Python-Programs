def generate_primes_up_to_n(n):
    primes = []
    for num in range(2, n + 1):
        if is_prime(num):
            primes.append(num)
    return primes

# Example usage
limit = int(input("Enter a limit (N) to generate prime numbers up to N: "))
prime_numbers = generate_primes_up_to_n(limit)
print(f"The prime numbers up to {limit} are: {prime_numbers}")