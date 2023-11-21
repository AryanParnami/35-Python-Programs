def find_average(numbers):
    return sum(numbers) / len(numbers)

# Example usage
numbers = [int(x) for x in input("Enter a set of integers separated by spaces: ").split()]
average = find_average(numbers)
print(f"The average is {average}.")