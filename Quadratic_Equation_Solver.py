import math

# Function to solve a quadratic equation
def solve_quadratic(a, b, c):
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c

    # Check if the roots are real or complex
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return f"Two distinct real roots: {root1} and {root2}"
    elif discriminant == 0:
        root = -b / (2*a)
        return f"One real root: {root}"
    else:
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(-discriminant) / (2*a)
        return f"Two complex roots: {real_part} ± {imaginary_part}i"

# Input coefficients from the user
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Solve the quadratic equation
result = solve_quadratic(a, b, c)
print(result)
