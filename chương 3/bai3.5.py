import numpy as np
def main():
    with open('chương 3/heights_1.txt', 'r') as file_height:
        height = [float(line.strip()) for line in file_height]

    with open('chương 3/weights_1.txt', 'r') as file_weight:
        weight = [float(line.strip()) for line in file_weight]

    arr_height = np.array(height)

    arr_weight = np.array(weight)

    he_so_quy_doi_height = 0.0254
    arr_height_m = arr_height * he_so_quy_doi_height

    he_so_quy_doi_weight = 0.453592
    arr_weight_kg = arr_weight * he_so_quy_doi_weight

    arr_bmi = arr_weight_kg / (arr_height_m ** 2)

    weight_at_index_50 = arr_weight_kg[50]

    arr_height_m_100 = arr_height_m[100:111]

    bmi_lt_21_indices = np.where(arr_bmi < 21)[0]

    average_height = np.mean(arr_height_m)
    average_weight = np.mean(arr_weight_kg)

    max_height = np.max(arr_height_m)
    max_weight = np.max(arr_weight_kg)

    min_height = np.min(arr_height_m)
    min_weight = np.min(arr_weight_kg)

    print("1. Numpy Array arr_height:")
    print(arr_height)

    print("\n2. Numpy Array arr_weight:")
    print(arr_weight)

    print("\n3. Numpy Array arr_height_m:")
    print(arr_height_m)

    print("\n4. Numpy Array arr_weight_kg:")
    print(arr_weight_kg)

    print("\n5. Numpy Array arr_bmi:")
    print(arr_bmi)

    print("\n6. Giá trị cân nặng ở vị trí index = 50 trong arr_weight_kg:")
    print(weight_at_index_50)

    print("\n7. Numpy Array arr_height_m_100:")
    print(arr_height_m_100)

    print("\n8. Các cầu thủ có bmi < 21 (index):")
    print(bmi_lt_21_indices)

    print("\n9. Chiều cao trung bình và cân nặng trung bình:")
    print("   Chiều cao trung bình:", average_height)
    print("   Cân nặng trung bình:", average_weight)

    print("\n10. Chiều cao và cân nặng lớn nhất của các cầu thủ:")
    print("    Chiều cao lớn nhất:", max_height)
    print("    Cân nặng lớn nhất:", max_weight)

    print("\n11. Chiều cao và cân nặng nhỏ nhất của các cầu thủ:")
    print("    Chiều cao nhỏ nhất:", min_height)
    print("    Cân nặng nhỏ nhất:", min_weight)
if __name__ == '__main__':
    main()