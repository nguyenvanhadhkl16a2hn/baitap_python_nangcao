import numpy as np

arr = np.arange(10)
print("1. Numpy Array arr:")
print(arr)
print("   Kiểu dữ liệu của arr:", arr.dtype)
print("   Kích thước của arr:", arr.shape)

arr_odd = arr[arr % 2 != 0]
arr_even = arr[arr % 2 == 0]

print("\n2. Numpy Arrays arr_odd và arr_even:")
print("   arr_odd:", arr_odd)
print("   arr_even:", arr_even)

arr_update_1 = np.where(arr % 2 != 0, 100, arr)

print("\n3. Numpy Array arr_update_1:")
print(arr_update_1)