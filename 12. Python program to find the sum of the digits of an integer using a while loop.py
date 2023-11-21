def sum_of_digits(number):
    total = 0
    while number > 0:
        total += number % 10
        number //= 10
    return total

# Example usage
num = int(input("Enter an integer: "))
digit_sum = sum_of_digits(num)
print(f"The sum of digits of {num} is {digit_sum}.")