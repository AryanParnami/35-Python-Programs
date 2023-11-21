def delete_element_by_index(arr, index):
    if 0 <= index < len(arr):
        del arr[index]

# Example usage
numbers = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]
index_to_delete = int(input("Enter the index to delete: "))
delete_element_by_index(numbers, index_to_delete)
print(f"The list after deleting the element at index {index_to_delete} is: {numbers}")
