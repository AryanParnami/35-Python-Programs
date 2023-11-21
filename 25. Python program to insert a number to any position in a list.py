def insert_number_at_position(arr, num, position):
    arr.insert(position, num)

# Example usage
numbers = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]
new_num = int(input("Enter the number to insert: "))
position = int(input("Enter the position to insert the number: "))
insert_number_at_position(numbers, new_num, position)
print(f"The list after inserting {new_num} at position {position} is: {numbers}")
