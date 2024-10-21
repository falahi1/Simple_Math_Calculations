# This code checks for numbers divisible by a given divisor within a specified range.

# Input the starting number, ending number, and divisor
num1 = int(input("Please enter the starting number: "))
num2 = int(input("Please enter the ending number: "))
divisor = int(input("Please enter the divisor: "))

# Check if the divisor is zero
if divisor == 0:
    print("Divisor cannot be zero.")
else:
    # Loop through the range and check for divisibility
    for i in range(num1, num2 + 1):
        if i % divisor == 0:
            print(i)
