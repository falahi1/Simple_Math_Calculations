# Function to calculate factorial
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Function to calculate e^x using Taylor series
def taylor_series_e_x(x, n):
    result = 1
    for i in range(1, n + 1):
        result += (x ** i) / factorial(i)
    return result

# Input x and number of terms n
x = float(input("Enter the value of x for e^x: "))
n = int(input("Enter the number of terms in the Taylor series: "))

# Calculate and output the result
print(f"The result of e^{x} using {n} terms of the Taylor series is: {taylor_series_e_x(x, n)}")
