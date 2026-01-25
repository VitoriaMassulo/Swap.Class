#Advanced (Algorithms & Performance)

def bubble_sort(numbers):
    # 'n' is the total number of items in our list
    n = len(numbers)
    
    # The Outer Loop: Controls how many times we walk through the list
    for i in range(n):
        # The Inner Loop: Compares neighbor elements
        # 'n - i - 1' makes the loop shorter each time because 
        # the largest numbers are already at the end!
        for j in range(0, n - i - 1):
            
            # 1. Compare: Is the current number bigger than the next one?
            if numbers[j] > numbers[j + 1]:
                
                # 2. Swap: If yes, they trade places!
                # This is the "Pythonic Swap" we talked about.
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                
    return numbers

# Testing the logic:
data = [5, 1, 4, 2]
sorted_data = bubble_sort(data)
print(f"Sorted list: {sorted_data}")


