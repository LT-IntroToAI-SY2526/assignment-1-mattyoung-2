# Assignment 1: AI-Generated Python Problems
# Name: [Matt Young]

"""
AI-Generated Problem Set

INSTRUCTIONS:
1. Document your original AI prompt below
2. Copy the problems your AI assistant generated
3. Implement solutions for each problem
4. Include comments explaining your approach
5. Test your solutions with different inputs

Remember: The goal is to LEARN, not just get working code!
"""

# =============================================================================
# PART 1: DOCUMENT YOUR AI COLLABORATION
# =============================================================================

"""
MY ORIGINAL AI PROMPT:
> "I'm learning Python basics in a high school programming class. I have some experience with [mention your previous programming language if any, or say 'I'm new to programming']. Can you create 5-7 practice problems that cover:
> - Variables and basic data types
> - Conditionals (if/elif/else)
> - Loops (for and while)
> - Functions
> - Basic list operations
> 
> Make them progressively more challenging. Make sure each problem has clear instructions and example inputs/outputs."

Example: "I'm learning Python basics in a high school programming class. 
I have some experience with Java. Can you create 5-7 practice problems that cover..."
"""

# =============================================================================
# PART 2: AI-GENERATED PROBLEMS & SOLUTIONS
# =============================================================================

"""
PROBLEM 1: [Write a program that takes two numbers from the user and prints their sum, difference, product, and quotient.]


Example:
Problem: Write a function called 'is_even' that takes an integer and returns 
True if the number is even, False if it's odd.

Example inputs/outputs:
- is_even(4) should return True
- is_even(7) should return False
"""
# Ask the user to enter two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform operations
sum_result = num1 + num2
difference = num1 - num2
product = num1 * num2

# Check for division by zero
if num2 != 0:
    quotient = num1 / num2
else:
    quotient = "Undefined (cannot divide by zero)"


# Print results
print("Sum:", sum_result)
print("Difference:", difference)
print("Product:", product)
print("Quotient:", quotient)


"""
 Problem 2: Calculate Area and Perimeter of Rectangle
 """

length = float(input("Enter the length: "))
width = float(input("Enter the width: "))

area = length * width
perimeter = 2 * (length + width)

print("Area:", area)
print("Perimeter:", perimeter)


"""Problem 3: Check if a number is negative, positive or 0

"""

num = float(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

"""Problem 4: Ask the user for two numbers and an operator (+, -, *, /). Perform the operation and print the result."""

num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Undefined (division by zero)"
else:
    result = "Invalid operator"

print("Result:", result)


"""Problem 5:Ask the user to enter a number N. Print all even numbers from 1 to N (inclusive).

"""
n = int(input("Enter a number: "))

print("Even numbers from 1 to", n)
for i in range(1, n + 1):
    if i % 2 == 0:
        print(i)



"""Problem 6: Write a function that takes a number as input and returns its square.

"""

def square(num):
    return num * num

# Get input and call function
number = float(input("Enter a number to square: "))
result = square(number)
print("Square:", result)


"""Problem 7:Ask the user to enter three numbers, and then print out the largest one.

"""

# Get three numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Compare the numbers
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

print("The largest number is:", largest)









# =============================================================================
# PART 3: TESTING YOUR SOLUTIONS
# =============================================================================


"""
Test all your solutions with different inputs

Add asserts if you feel comfortable

Example:
print("Testing Problem 1:")
print(f"is_even(4): {is_even(4)}")  # Should print True
print(f"is_even(7): {is_even(7)}")  # Should print False
"""

# --------------------------------------
# Problem 1: Basic Math Operations
# --------------------------------------
def basic_math_ops(a, b):
    sum_result = a + b
    diff = a - b
    prod = a * b
    quot = a / b if b != 0 else None
    return (sum_result, diff, prod, quot)

print("Testing Problem 1:")
print(f"basic_math_ops(10, 5): {basic_math_ops(10, 5)}")  # (15, 5, 50, 2.0)
print(f"basic_math_ops(7, 0): {basic_math_ops(7, 0)}")    # (7, 7, 0, None)
assert basic_math_ops(10, 5) == (15, 5, 50, 2.0)
assert basic_math_ops(7, 0) == (7, 7, 0, None)

# --------------------------------------
# Problem 2: Number Sign
# --------------------------------------
def number_sign(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"

print("\nTesting Problem 2:")
print(f"number_sign(3): {number_sign(3)}")     # Positive
print(f"number_sign(-10): {number_sign(-10)}") # Negative
print(f"number_sign(0): {number_sign(0)}")     # Zero
assert number_sign(3) == "Positive"
assert number_sign(-10) == "Negative"
assert number_sign(0) == "Zero"

# --------------------------------------
# Problem 3: Simple Calculator
# --------------------------------------
def simple_calculator(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        return a / b if b != 0 else None
    else:
        return "Invalid"

print("\nTesting Problem 3:")
print(f"simple_calculator(4, 2, '+'): {simple_calculator(4, 2, '+')}")  # 6
print(f"simple_calculator(9, 3, '/'): {simple_calculator(9, 3, '/')}")  # 3.0
print(f"simple_calculator(5, 0, '/'): {simple_calculator(5, 0, '/')}")  # None
print(f"simple_calculator(2, 3, '^'): {simple_calculator(2, 3, '^')}")  # Invalid
assert simple_calculator(4, 2, "+") == 6
assert simple_calculator(9, 3, "/") == 3.0
assert simple_calculator(5, 0, "/") == None
assert simple_calculator(2, 3, "^") == "Invalid"

# --------------------------------------
# Problem 4: Get Even Numbers from 1 to N
# --------------------------------------
def get_even_numbers(n):
    return [i for i in range(1, n + 1) if i % 2 == 0]

print("\nTesting Problem 4:")
print(f"get_even_numbers(10): {get_even_numbers(10)}")  # [2, 4, 6, 8, 10]
print(f"get_even_numbers(5): {get_even_numbers(5)}")    # [2, 4]
print(f"get_even_numbers(1): {get_even_numbers(1)}")    # []
assert get_even_numbers(10) == [2, 4, 6, 8, 10]
assert get_even_numbers(5) == [2, 4]
assert get_even_numbers(1) == []

# --------------------------------------
# Problem 5: Square a Number
# --------------------------------------
def square(num):
    return num * num

print("\nTesting Problem 5:")
print(f"square(2): {square(2)}")     # 4
print(f"square(-3): {square(-3)}")   # 9
print(f"square(0): {square(0)}")     # 0
assert square(2) == 4
assert square(-3) == 9
assert square(0) == 0
