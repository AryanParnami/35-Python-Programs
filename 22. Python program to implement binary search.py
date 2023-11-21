def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_element = arr[mid]

        if mid_element == target:
            return mid
        elif mid_element < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# Example usage
numbers = sorted([int(x) for x in input("Enter a sorted list of numbers separated by spaces: ").split()])
target_number = int(input("Enter the number to search: "))
result = binary_search(numbers, target_number)

if result != -1:
    print(f"{target_number} found at index {result}.")
else:
    print(f"{target_number} not found in the list.")
