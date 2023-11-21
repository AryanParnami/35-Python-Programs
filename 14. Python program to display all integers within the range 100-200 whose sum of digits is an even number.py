start = 100
end = 200

def is_sum_of_digits_even(number):
    return sum(int(digit) for digit in str(number)) % 2 == 0

result = [num for num in range(start, end + 1) if is_sum_of_digits_even(num)]
print(f"The integers in the range {start} to {end} with even sum of digits are: {result}")