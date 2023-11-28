import numpy as np

# Đọc dữ liệu từ tập tin heights.txt và positions.txt
with open('chương 3/heights.txt', 'r') as file_heights, open('chương 3/positions.txt', 'r') as file_positions:
    heights = [float(line.strip()) for line in file_heights]
    positions = [line.strip() for line in file_positions]

# 1a: Tạo numpy array np_positions từ list positions
np_positions = np.array(positions, dtype='U5')
print("1a. Kiểu dữ liệu của np_positions:", np_positions.dtype)

# 1b: Tạo numpy array np_heights từ list heights
np_heights = np.array(heights, dtype=float)
print("1b. Kiểu dữ liệu của np_heights:", np_heights.dtype)

# 2: Tính chiều cao trung bình của các GK
average_height_gk = np.mean(np_heights[np_positions == 'GK'])
print("\n2. Chiều cao trung bình của các GK:", average_height_gk)

# 3: Tính chiều cao trung bình của những vị trí khác (Không phải là GK)
average_height_other = np.mean(np_heights[np_positions != 'GK'])
print("\n3. Chiều cao trung bình của những vị trí khác:", average_height_other)

# 4: Tạo mảng dữ liệu có cấu trúc tự định nghĩa 'players'
players = np.array(list(zip(np_positions, np_heights)), dtype=[('position', 'U5'), ('height', float)])
print("\n4. Mảng dữ liệu players:")
print(players)

# 5: Sắp mảng players theo height
players_sorted = np.sort(players, order='height')
max_height_position = players_sorted[-1]['position']
min_height_position = players_sorted[0]['position']

print("\n5. Vị trí có chiều cao cao nhất:", max_height_position)
print("   Vị trí có chiều cao thấp nhất:", min_height_position)