import numpy as np

arr = np.arange(1, 11)
print("Original Array:", arr)

print("\nFirst five elements:", arr[:5])
print("Elements from index 3 to 7:", arr[3:8])
print("Alternate elements:", arr[::2])
print("Array in reverse order:", arr[::-1])

print("\nSum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))

add_arr = arr + 5
print("\nArray after adding 5:", add_arr)

mul_arr = arr * 2
print("Array after multiplying by 2:", mul_arr)