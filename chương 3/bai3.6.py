import numpy as np
def main():
    arr = np.full((3, 3), True, dtype=bool)
    arr_1D = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])
    arr_2D = arr_1D.reshape(3, 3)
    arr_2D[:, [0, 2]] = arr_2D[:, [2, 0]]
    arr_2D[[0, 1], :] = arr_2D[[1, 0], :]
    arr_2D = arr_2D[::-1, :]
    arr_2D = arr_2D[:, ::-1]
    arr_2D_null = np.array([[1, 2, 3], [np.NaN, 5, 6], [7, np.NaN, 9], [4, 5, 6]])
    has_nan = np.isnan(arr_2D_null).any()
    arr_2D_null[np.isnan(arr_2D_null)] = 0
    print("1. Numpy Array arr:")
    print(arr)
    print("\n2. Numpy Array arr_2D (sau khi chuyển cột):")
    print(arr_2D)
    print("\n3. Numpy Array arr_2D (sau khi chuyển dòng):")
    print(arr_2D)
    print("\n4. Numpy Array arr_2D (sau khi đảo ngược các dòng):")
    print(arr_2D)
    print("\n5. Numpy Array arr_2D (sau khi đảo ngược các cột):")
    print(arr_2D)
    print("\n6. Trong array có giá trị rỗng không? ", has_nan)
    print("\n7. Numpy Array arr_2D_null (sau khi thay thế giá trị null):")
    print(arr_2D_null)
if __name__ == '__main__':
    main()