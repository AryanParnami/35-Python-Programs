def print_dictionary_items(dictionary):
    for key, value in dictionary.items():
        print(f"{key}: {value}")

# Example usage
my_dict = {"name": "John", "age": 25, "city": "New York"}
print("Items in the dictionary:")
print_dictionary_items(my_dict)
