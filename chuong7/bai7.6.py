import tkinter as tk

# Tạo một cửa sổ mới
window = tk.Tk()

# Thiết lập tiêu đề cho cửa sổ
window.title("Chương trình đảo ngược chuỗi")

# Thiết lập kích thước cho cửa sổ
window.geometry("400x200")

# Tạo một nhãn để hiển thị hướng dẫn cho người dùng
label = tk.Label(window, text="Nhập chuỗi cần đảo ngược:")
label.pack()

# Tạo một hộp văn bản để người dùng nhập chuỗi
entry = tk.Entry(window)
entry.pack()

# Tạo một hàm để đảo ngược chuỗi
def reverse_string():
    # Lấy chuỗi từ hộp văn bản
    chuoi = entry.get()

    # Khởi tạo một chuỗi rỗng để lưu kết quả
    ket_qua = ""

    # Lặp qua từng ký tự trong chuỗi và thêm chúng vào đầu chuỗi kết quả
    for ky_tu in chuoi:
        ket_qua = ky_tu + ket_qua

    # Hiển thị chuỗi kết quả
    result_label.config(text="Chuỗi đảo ngược là: " + ket_qua)

# Tạo một nút để kích hoạt hàm đảo ngược chuỗi
button = tk.Button(window, text="Đảo ngược chuỗi", command=reverse_string)
button.pack()

# Tạo một nhãn để hiển thị kết quả
result_label = tk.Label(window, text="")
result_label.pack()

# Chạy chương trình
window.mainloop()

