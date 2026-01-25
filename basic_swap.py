#1. The "Temporary Variable" Method (The Standard Way)

a = int(input("Enter A: "))
b = int(input("Enter B: "))

print(f"Before: a = {a}, b = {b}")

# The Swap Logic
temp = a   # Step 1: Save 'a' in a temporary 'box'
a = b      # Step 2: Put 'b' into 'a'
b = temp   # Step 3: Put the saved value from 'temp' into 'b'

print(f"After:  a = {a}, b = {b}")

