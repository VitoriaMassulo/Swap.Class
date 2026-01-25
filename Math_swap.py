#The Arithmetic Method (Sum and Difference)
#You can use addition and subtraction to track the "difference" between the two numbers.

a = int(input("Enter A: ")) # Example: 5
b = int(input("Enter B: ")) # Example: 10

# 1. Add them together and store in 'a'
a = a + b  # a is now 15 (5 + 10)

# 2. Subtract the new 'b' from the new 'a'
b = a - b  # b is now 5 (15 - 10) -> original 'a'!

# 3. Subtract the new 'b' from the new 'a' again
a = a - b  # a is now 10 (15 - 5) -> original 'b'!

print(f"Swapped: a = {a}, b = {b}")
