import tkinter as tk

# Tạo một cửa sổ mới
window = tk.Tk()

# Thiết lập tiêu đề cho cửa sổ
window.title("Liệt kê các ước số của một số nguyên")

# Thiết lập kích thước cho cửa sổ
window.geometry("400x200")

# Tạo một nhãn để hiển thị hướng dẫn cho người dùng
label = tk.Label(window, text="Nhập số nguyên N:")
label.pack()

# Tạo một hộp văn bản để người dùng nhập số nguyên N
entry = tk.Entry(window)
entry.pack()

# Tạo một hàm để liệt kê các ước của N
def calculate_divisors():
    # Lấy số nguyên N từ hộp văn bản
    n = int(entry.get())

    # Khởi tạo danh sách ước số
    divisors = []

    # Duyệt qua các số từ 1 đến N và kiểm tra xem số đó có phải là ước của N hay không
    for i in range(1, n+1):
        if n % i == 0:
            divisors.append(i)

    # Hiển thị danh sách ước số
    result_label.config(text="Các ước số của " + str(n) + " là: " + str(divisors))

# Tạo một nút để kích hoạt hàm liệt kê các ước của N
button = tk.Button(window, text="Liệt kê các ước số", command=calculate_divisors)
button.pack()

# Tạo một nhãn để hiển thị kết quả
result_label = tk.Label(window, text="")
result_label.pack()

# Chạy chương trình
window.mainloop()
