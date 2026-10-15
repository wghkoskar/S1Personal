# Worksheet 1.2: Task 2 Solution
import sys
from util import read_numbers
try:
    numbers = read_numbers()
    print(f"Minimum = {min(numbers)}") # Outputs minimum number
    print(f"Maximum = {max(numbers)}") # Outputs maximum number
    print(f"Mean = {sum(numbers) / len(numbers)}") # Divides the sum / length to find 
    numbers.sort() # Sorts the list
    medianPosition = len(numbers) // 2
    if len(numbers) % 2 == 0: # If/else tree handles whether it is an odd or even
        print(f"Median = {(numbers[medianPosition - 1] + numbers[medianPosition]) / 2}")
    else:
        print(f"Median = {numbers[medianPosition]}")
except:
    sys.exit("Error: no numbers provided")