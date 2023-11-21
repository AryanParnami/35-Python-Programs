def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Example usage
numbers = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]
target_number = int(input("Enter the number to search: "))
result = linear_search(numbers, target_number)

if result != -1:
    print(f"{target_number} found at index {result}.")
else:
    print(f"{target_number} not found in the list.")
