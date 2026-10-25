import pandas as pd
import numpy as np

np.random.seed(42)
numbers = np.random.randint(1, 100, 10)

s = pd.Series(numbers)
print("Original Series:")
print(s)

print("\nElement at index 3:", s[3])
print("First five elements:")
print(s[:5])

print("\nNumbers greater than 50:")
print(s[s > 50])

print("\nMean:", s.mean())
print("Median:", s.median())
print("Minimum:", s.min())
print("Maximum:", s.max())