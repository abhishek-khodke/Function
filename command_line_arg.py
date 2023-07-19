import sys

# Check if we have exactly 5 arguments
if len(sys.argv) != 6:
    print("Error: please provide exactly 5 numbers as arguments")
    sys.exit(1)

# Extract the numbers from the arguments and convert them to floats
numbers = [float(arg) for arg in sys.argv[1:]]

# Calculate the sum of the numbers
total = sum(numbers)

# Print the result
print("The sum of the numbers is:", total)
