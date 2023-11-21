import cmath

def quadratic_roots(a, b, c):
    # Calculate the discriminant
    d = cmath.sqrt(b**2 - 4*a*c)

    # Compute the two roots
    root1 = (-b + d) / (2 * a)
    root2 = (-b - d) / (2 * a)

    return root1, root2

# Example usage
a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))

roots = quadratic_roots(a, b, c)
print(f"The roots of the quadratic equation are: {roots}")
