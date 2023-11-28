import numpy as np
def main():
    # Đọc dữ liệu từ tập tin baseball_2D.txt
    with open('chương 3/baseball_2D.txt', 'r') as file:
        baseball = [line.strip().split() for line in file]

    # Chuyển danh sách thành mảng NumPy 2D
    np_baseball = np.array(baseball, dtype=float)

    # Câu 1: Xem kiểu dữ liệu và kích thước của np_baseball
    print("1. Kiểu dữ liệu của np_baseball:", np_baseball.dtype)
    print("   Kích thước của np_baseball:", np_baseball.shape)

    # Câu 2: In các giá trị của dòng thứ 50 trong np_baseball
    print("\n2. Dữ liệu của dòng thứ 50 trong np_baseball:")
    print(np_baseball[49, :])

    # Câu 3: Tạo numpy array np_weight với dữ liệu từ cột 2 của np_baseball
    np_weight = np_baseball[:, 1]

    # Câu 4: Chiều cao của vận động viên thứ 124
    height_of_player_124 = np_baseball[123, 0]
    print("\n4. Chiều cao của vận động viên thứ 124:", height_of_player_124)

    # Câu 5: Chiều cao trung bình và cân nặng trung bình của các cầu thủ
    average_height = np.mean(np_baseball[:, 0])
    average_weight = np.mean(np_baseball[:, 1])
    print("\n5. Chiều cao trung bình của các cầu thủ:", average_height)
    print("   Cân nặng trung bình của các cầu thủ:", average_weight)

    # Câu 6: Mối tương quan giữa chiều cao và cân nặng
    correlation = np.corrcoef(np_baseball[:, 0], np_baseball[:, 1])[0, 1]

    print("\n6. Mối tương quan giữa chiều cao và cân nặng:")
    if correlation > 0:
        print("   Có tương quan thuận.")
    elif correlation < 0:
        print("   Có tương quan nghịch.")
    else:
        print("   Không có tương quan.")
if __name__ == '__main__':
    main()