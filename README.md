🔄 The Art of Swapping in Python

This repository is a comprehensive study of variable swapping techniques, ranging from fundamental logic to advanced sorting algorithms. 
📖 Introduction
Swapping is the process of exchanging the values of two variables. While it seems simple, it is the building block for data manipulation and memory management.

---
🛠️ Techniques & Implementations

1. The Temporary Variable Method (Classic)
This is the standard approach used in most programming languages. It uses a "third glass" to hold the value.

```python
# basic_swap.py
a = 5
b = 10

temp = a
a = b
b = temp

2. The Arithmetic Method (No Extra Variables)
A logic trick using math to swap values without needing extra memory.
# math_swap.py
a = a + b
b = a - b
a = a - b

3. The Pythonic Method (Best Practice)
Using Tuple Unpacking for clean and efficient code.
# pythonic_swap.py
a, b = b, a

🎓 Advanced Application: Bubble Sort
The most famous use of swapping is in Sorting Algorithms. Bubble Sort works by repeatedly swapping adjacent elements if they are in the wrong order.

Implementation Code:
# bubble_sort.py
data = [64, 34, 25, 12, 22, 11, 90]
n = len(data)

for i in range(n):
    for j in range(0, n - i - 1):
        if data[j] > data[j + 1]:
            # Strategic Swap
            data[j], data[j + 1] = data[j + 1], data[j]

print("Final Result:", data)

🧠 Lessons Learned
 * Memory Management: Understanding when to use a temporary variable.
 * Algorithm Efficiency: How multiple swaps lead to an organized data structure.
 * Pythonic Syntax: Leveraging Python's unique features to write less code.
Organized for study purposes by Vitoria Massulo

---







