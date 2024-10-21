from statistics import mean, median, mode

# Input a list of numbers from the user
numbers = list(map(float, input("Enter a list of numbers separated by spaces: ").split()))

# Calculate and output mean, median, and mode
print(f"Mean: {mean(numbers)}")
print(f"Median: {median(numbers)}")

try:
    print(f"Mode: {mode(numbers)}")
except:
    print("No mode found (all numbers appear the same number of times).")
