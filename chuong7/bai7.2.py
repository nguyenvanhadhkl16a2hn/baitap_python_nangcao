import tkinter as tk
# Tạo một cửa sổ mới
window = tk.Tk()
# Đặt tiêu đề cho cửa sổ
window.title("Tiêu đề của cửa sổ")
# Tạo một nhãn cho cửa sổ
label = tk.Label(window, text="Đây là một nhãn dán!")
label.pack()
# Hiển thị cửa sổ
window.mainloop()
  