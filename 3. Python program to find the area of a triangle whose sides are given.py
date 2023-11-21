def area_of_triangle(side1, side2, side3):
    # Using Heron's formula
    s = (side1 + side2 + side3) / 2
    area = (s * (s - side1) * (s - side2) * (s - side3)) ** 0.5
    return area

# Example usage
a = float(input("Enter the length of side 1: "))
b = float(input("Enter the length of side 2: "))
c = float(input("Enter the length of side 3: "))
triangle_area = area_of_triangle(a, b, c)
print(f"The area of the triangle is {triangle_area}.")