import tkinter as tk
from lunarcalendar import Converter

# Tạo một cửa sổ mới
window = tk.Tk()

# Thiết lập tiêu đề cho cửa sổ
window.title("Chuyển đổi năm dương lịch sang năm âm lịch")

# Thiết lập kích thước cho cửa sổ
window.geometry("400x200")

# Tạo một nhãn để hiển thị hướng dẫn cho người dùng
label = tk.Label(window, text="Nhập năm dương lịch:")
label.pack()

# Tạo một hộp văn bản để người dùng nhập năm dương lịch
entry = tk.Entry(window)
entry.pack()

# Tạo một hàm để tính năm âm lịch tương ứng
def calculate():
    # Lấy năm dương lịch từ hộp văn bản
    year = int(entry.get())

    # Tính năm âm lịch tương ứng
    lunar = Converter().solar_to_lunar(year, 1, 1)

    # Hiển thị kết quả
    result_label.config(text="Năm âm lịch tương ứng là: " + str(lunar[0]) + " - " + lunar[1])

# Tạo một nút để kích hoạt hàm tính năm âm lịch tương ứng
button = tk.Button(window, text="Chuyển đổi", command=calculate)
button.pack()

# Tạo một nhãn để hiển thị kết quả
result_label = tk.Label(window, text="")
result_label.pack()

# Chạy chương trình
window.mainloop()
