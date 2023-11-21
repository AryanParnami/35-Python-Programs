def is_multiple_of_5(number):
    return number % 5 == 0

# Example usage
num = int(input("Enter an integer: "))
if is_multiple_of_5(num):
    print(f"{num} is a multiple of 5.")
else:
    print(f"{num} is not a multiple of 5.")
