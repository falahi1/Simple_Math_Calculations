# Function to generate Fibonacci sequence
def fibonacci(n):
    sequence = [0, 1]
    for i in range(2, n):
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)
    return sequence

# Input the number of terms from the user
terms = int(input("Enter the number of Fibonacci terms to generate: "))

# Generate and display the Fibonacci sequence
if terms <= 0:
    print("Please enter a positive number.")
else:
    fib_sequence = fibonacci(terms)
    print(f"Fibonacci sequence: {fib_sequence}")
