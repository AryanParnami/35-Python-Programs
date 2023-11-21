def calculator(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Cannot divide by zero."
    else:
        return "Invalid operation."

# Example usage
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
op = input("Enter the operation (+, -, *, /): ")
result = calculator(number1, number2, op)
print(f"The result of the operation is: {result}")
