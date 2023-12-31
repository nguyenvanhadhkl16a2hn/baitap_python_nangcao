import tkinter as tk

# Tạo một cửa sổ mới
window = tk.Tk()

# Thiết lập tiêu đề cho cửa sổ
window.title("Tính chỉ số BMI")

# Thiết lập kích thước cho cửa sổ
window.geometry("400x200")

# Tạo một nhãn để hiển thị hướng dẫn cho người dùng
label1 = tk.Label(window, text="Nhập cân nặng của bạn (kg):")
label1.pack()

# Tạo một hộp văn bản để người dùng nhập cân nặng của họ
entry1 = tk.Entry(window)
entry1.pack()

# Tạo một nhãn để hiển thị hướng dẫn cho người dùng
label2 = tk.Label(window, text="Nhập chiều cao của bạn (m):")
label2.pack()

# Tạo một hộp văn bản để người dùng nhập chiều cao của họ
entry2 = tk.Entry(window)
entry2.pack()

# Tạo một hàm để tính chỉ số BMI tương ứng
def calculate():
    # Lấy cân nặng và chiều cao từ hộp văn bản
    weight = float(entry1.get())
    height = float(entry2.get())

    # Tính chỉ số BMI tương ứng
    bmi = weight / (height ** 2)

    # Hiển thị kết quả
    result_label.config(text="Chỉ số BMI của bạn là: " + str(round(bmi, 2)))

    # Hiển thị thông báo kết luận theo chỉ số BMI
    if bmi < 18.5:
        conclusion_label.config(text="Bạn đang gầy và cần tăng cân.")
    elif bmi < 25:
        conclusion_label.config(text="Bạn có thể nói là cân đối.")
    elif bmi < 30:
        conclusion_label.config(text="Bạn đang thừa cân và cần giảm cân.")
    else:
        conclusion_label.config(text="Bạn đang béo phì và cần giảm cân.")

# Tạo một nút để kích hoạt hàm tính chỉ số BMI tương ứng
button = tk.Button(window, text="Tính", command=calculate)
button.pack()

# Tạo một nhãn để hiển thị kết quả
result_label = tk.Label(window, text="")
result_label.pack()

# Tạo một nhãn để hiển thị thông báo kết luận theo chỉ số BMI
conclusion_label = tk.Label(window, text="")
conclusion_label.pack()

# Chạy chương trình
window.mainloop()
 