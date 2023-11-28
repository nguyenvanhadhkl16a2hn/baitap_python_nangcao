import numpy as np

# 1: 
arr_zeros = np.zeros(10)
arr_zeros[4] = 1

print("1. Numpy Array arr_zeros:")
print(arr_zeros)

# 2: 
arr_h = np.arange(10, 25)
arr_h_reverse = np.flip(arr_h)

print("\n2. Numpy Array arr_h (đảo ngược):")
print(arr_h_reverse)

# 3: 
arr_k = np.array([1, 2, 0, 8, 2, 0, 1, 3, 0, 5, 0])
arr_l = arr_k[arr_k != 0]

print("\n3. Numpy Array arr_l:")
print(arr_l)

# 4: 
arr_l = np.append(arr_l, [10, 20])

print("\n4. Numpy Array arr_l sau khi thêm 10 và 20:")
print(arr_l)

# 5:  
arr_l = np.insert(arr_l, 5, 100)

print("\n5. Numpy Array arr_l sau khi thêm phần tử 100:")
print(arr_l)

# 6: 
arr_l = np.delete(arr_l, [0, 1, 2])

print("\n6. Numpy Array arr_l sau khi xóa các phần tử tại index 0, 1, 2:")
print(arr_l)