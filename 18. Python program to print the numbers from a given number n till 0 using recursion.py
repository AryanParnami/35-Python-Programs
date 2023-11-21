def print_numbers_from_n_to_0(n):
    if n < 0:
        return
    print(n, end=" ")
    print_numbers_from_n_to_0(n - 1)

# Example usage
num = int(input("Enter a number: "))
print(f"Numbers from {num} to 0 are:")
print_numbers_from_n_to_0(num)
