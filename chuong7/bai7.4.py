import tkinter as tk

def submit():
    name = name_entry.get()
    id = id_entry.get()
    password = password_entry.get()
    print(f"Name: {name}\nID: {id}\nPassword: {password}")

# Tạo một cửa sổ mới
window = tk.Tk()

# Đặt tiêu đề cho cửa sổ
window.title("Đăng nhập")

# Tạo các hộp văn bản
name_label = tk.Label(window, text="Tên sinh viên:")
name_label.grid(column=0, row=0)
name_entry = tk.Entry(window)
name_entry.grid(column=1, row=0)

id_label = tk.Label(window, text="ID sinh viên:")
id_label.grid(column=0, row=1)
id_entry = tk.Entry(window)
id_entry.grid(column=1, row=1)

password_label = tk.Label(window, text="Mật khẩu:")
password_label.grid(column=0, row=2)
password_entry = tk.Entry(window, show="*")
password_entry.grid(column=1, row=2)

# Tạo nút Gửi
submit_button = tk.Button(window, text="Gửi", command=submit)
submit_button.grid(column=0, row=3, columnspan=2)

# Hiển thị cửa sổ
window.mainloop()
