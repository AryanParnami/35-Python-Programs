def find_largest_number(arr):
    if not arr:
        return None

    max_number = arr[0]
    for num in arr:
        if num > max_number:
            max_number = num

    return max_number

# Example usage
numbers = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]
largest_number = find_largest_number(numbers)
print(f"The largest number in the list is: {largest_number}")
