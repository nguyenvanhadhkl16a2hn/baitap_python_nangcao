import tkinter as tk

# Tạo một cửa sổ mới
window = tk.Tk()

# Thiết lập tiêu đề cho cửa sổ
window.title("Nhập tên và tuổi của bạn")

# Thiết lập kích thước cho cửa sổ
window.geometry("400x200")

# Tạo một nhãn để hiển thị hướng dẫn cho người dùng
label1 = tk.Label(window, text="Nhập tên của bạn:")
label1.pack()

# Tạo một hộp văn bản để người dùng nhập tên của họ
entry1 = tk.Entry(window)
entry1.pack()

# Tạo một nhãn để hiển thị hướng dẫn cho người dùng
label2 = tk.Label(window, text="Nhập tuổi của bạn:")
label2.pack()

# Tạo một hộp văn bản để người dùng nhập tuổi của họ
entry2 = tk.Entry(window)
entry2.pack()

# Tạo một hàm để xử lý thông tin người dùng
def process():
    # Lấy tên và tuổi từ hộp văn bản
    name = entry1.get()
    age = int(entry2.get())

    # Tạo thông báo dựa trên tuổi của người dùng
    if age >= 18:
        message = "Xin chào " + name + "! Bạn đã trưởng thành."
    else:
        message = "Xin chào " + name + "! Bạn còn nhỏ tuổi."

    # Hiển thị thông báo
    result_label.config(text=message)

# Tạo một nút để kích hoạt hàm xử lý thông tin người dùng
button = tk.Button(window, text="Xác nhận", command=process)
button.pack()

# Tạo một nhãn để hiển thị kết quả
result_label = tk.Label(window, text="")
result_label.pack()

# Chạy chương trình
window.mainloop()
