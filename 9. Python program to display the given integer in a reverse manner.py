def reverse_integer(number):
    return int(str(number)[::-1])

# Example usage
num = int(input("Enter an integer: "))
reversed_num = reverse_integer(num)
print(f"The reverse of {num} is {reversed_num}.")
