# Function to calculate factorial iteratively
def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Function to calculate factorial recursively
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

# Input a number from the user
num = int(input("Enter a number to calculate its factorial: "))

# Output the results
print(f"Factorial of {num} (Iterative): {factorial_iterative(num)}")
print(f"Factorial of {num} (Recursive): {factorial_recursive(num)}")
