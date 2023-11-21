def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Example usage
temp_celsius = float(input("Enter temperature in Celsius: "))
temp_fahrenheit = celsius_to_fahrenheit(temp_celsius)
print(f"{temp_celsius} Celsius is equal to {temp_fahrenheit} Fahrenheit.")