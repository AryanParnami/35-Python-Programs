import math

def geometric_mean(numbers):
    product = 1
    for num in numbers:
        product *= num
    return math.pow(product, 1/len(numbers))

# Example usage
numbers = [float(x) for x in input("Enter a set of numbers separated by spaces: ").split()]
geometric_mean_value = geometric_mean(numbers)
print(f"The geometric mean is {geometric_mean_value}.")
