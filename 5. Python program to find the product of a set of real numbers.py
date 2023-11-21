def find_product(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

# Example usage
numbers = [float(x) for x in input("Enter a set of real numbers separated by spaces: ").split()]
product = find_product(numbers)
print(f"The product is {product}.")