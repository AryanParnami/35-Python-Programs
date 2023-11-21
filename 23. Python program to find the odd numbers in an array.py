def find_odd_numbers(arr):
    return [num for num in arr if num % 2 != 0]

# Example usage
numbers = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]
odd_numbers = find_odd_numbers(numbers)
print(f"The odd numbers in the list are: {odd_numbers}")
