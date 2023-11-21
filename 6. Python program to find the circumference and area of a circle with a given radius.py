import math

def circle_properties(radius):
    circumference = 2 * math.pi * radius
    area = math.pi * radius**2
    return circumference, area

# Example usage
r = float(input("Enter the radius of the circle: "))
circumference, area = circle_properties(r)
print(f"The circumference of the circle is {circumference} and the area is {area}.")