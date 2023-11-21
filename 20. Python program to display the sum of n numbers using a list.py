def sum_of_numbers(n):
    numbers = [int(input(f"Enter number {i + 1}: ")) for i in range(n)]
    return sum(numbers)

# Example usage
count = int(input("Enter the count of numbers: "))
total_sum = sum_of_numbers(count)
print(f"The sum of the numbers is {total_sum}.")
