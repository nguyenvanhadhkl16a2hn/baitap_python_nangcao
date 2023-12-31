import tkinter as tk

# Tạo một cửa sổ mới
window = tk.Tk()

# Thiết lập tiêu đề cho cửa sổ
window.title("Tính tổng các số từ 1 đến N")

# Thiết lập kích thước cho cửa sổ
window.geometry("400x200")

# Tạo một nhãn để hiển thị hướng dẫn cho người dùng
label = tk.Label(window, text="Nhập số nguyên N:")
label.pack()

# Tạo một hộp văn bản để người dùng nhập số nguyên N
entry = tk.Entry(window)
entry.pack()

# Tạo một hàm để tính tổng các số từ 1 đến N
def calculate_sum():
    # Lấy số nguyên N từ hộp văn bản
    n = int(entry.get())

    # Tính tổng các số từ 1 đến N
    total = sum(range(1, n+1))

    # Tạo chuỗi kết quả
    result_string = "+".join(str(i) for i in range(1, n+1))

    # Hiển thị kết quả
    result_label.config(text="Tổng các số từ 1 đến " + str(n) + " là: " + result_string + " = " + str(total))

# Tạo một nút để kích hoạt hàm tính tổng
button = tk.Button(window, text="Tính tổng", command=calculate_sum)
button.pack()

# Tạo một nhãn để hiển thị kết quả
result_label = tk.Label(window, text="")
result_label.pack()

# Chạy chương trình
window.mainloop()

