def is_multiple_of_5_and_7(number):
    return number % 5 == 0 and number % 7 == 0

# Example usage
num = int(input("Enter an integer: "))
if is_multiple_of_5_and_7(num):
    print(f"{num} is a multiple of both 5 and 7.")
else:
    print(f"{num} is not a multiple of both 5 and 7.")
