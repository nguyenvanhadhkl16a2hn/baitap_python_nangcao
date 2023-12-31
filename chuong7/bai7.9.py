import tkinter as tk
from math import gcd

# Tạo một cửa sổ mới
window = tk.Tk()

# Thiết lập tiêu đề cho cửa sổ
window.title("Tính GCD và LCM")

# Thiết lập kích thước cho cửa sổ
window.geometry("400x200")

# Tạo một nhãn để hiển thị hướng dẫn cho người dùng
label = tk.Label(window, text="Nhập hai số nguyên:")
label.pack()

# Tạo hai hộp văn bản để người dùng nhập hai số nguyên
entry1 = tk.Entry(window)
entry1.pack()

entry2 = tk.Entry(window)
entry2.pack()

# Tạo một biến kiểu IntVar để lưu trữ lựa chọn của người dùng
choice = tk.IntVar()

# Tạo hai nút để cho phép người dùng chọn tính GCD hoặc LCM
gcd_button = tk.Radiobutton(window, text="Tính GCD", variable=choice, value=1)
gcd_button.pack()

lcm_button = tk.Radiobutton(window, text="Tính LCM", variable=choice, value=2)
lcm_button.pack()

# Tạo một hàm để tính GCD hoặc LCM tùy thuộc vào lựa chọn của người dùng
def calculate():
    # Lấy hai số nguyên từ hộp văn bản
    a = int(entry1.get())
    b = int(entry2.get())

    # Tính GCD hoặc LCM tùy thuộc vào lựa chọn của người dùng
    if choice.get() == 1:
        result = gcd(a, b)
    else:
        result = a * b // gcd(a, b)

    # Hiển thị kết quả
    result_label.config(text="Kết quả là: " + str(result))

# Tạo một nút để kích hoạt hàm tính GCD hoặc LCM
button = tk.Button(window, text="Tính", command=calculate)
button.pack()

# Tạo một nhãn để hiển thị kết quả
result_label = tk.Label(window, text="")
result_label.pack()

# Chạy chương trình
window.mainloop()
