# A simple calculator for basic arithmetic, root calculation, and power

# Prompt the user to choose an operation
operator = int(input(
    "Please choose the operation to compute: \n"
    "1 for Addition, \n2 for Subtraction, \n3 for Multiplication, \n"
    "4 for Division, \n5 for Root Calculation, \n6 for Power: "
))

# Perform the chosen arithmetic operation
if operator in [1, 2, 3, 4]:
    n1 = float(input("Please enter num1: "))
    n2 = float(input("Please enter num2: "))
    if operator == 1:
        result = n1 + n2  # Addition
    elif operator == 2:
        result = n1 - n2  # Subtraction
    elif operator == 3:
        result = n1 * n2  # Multiplication
    elif operator == 4:
        if n2 == 0:
            result = "Cannot divide by zero!"  # Handle division by zero
        else:
            result = n1 / n2  # Division

# Perform root calculation
elif operator == 5:
    n1 = float(input("Please enter the number: "))
    n2 = float(input("Please enter the root (e.g., 2 for square root): "))
    if n1 < 0 and n2 % 2 == 0:
        result = "Cannot compute root of a negative number for an even root."
    else:
        result = n1 ** (1 / n2)  # Root calculation

# Perform power calculation
elif operator == 6:
    n1 = float(input("Please enter the number: "))
    n2 = float(input("Please enter the power: "))
    result = n1 ** n2  # Exponentiation

else:
    result = "Invalid operation selected!"  # Handle invalid input

# Output the result
print("The result is:", result)
