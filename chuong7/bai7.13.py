import tkinter as tk
from tkinter import messagebox

class BaiTap:
    def __init__(self, chuong, bai_tap, tieu_de, noi_dung):
        self.chuong = chuong
        self.bai_tap = bai_tap
        self.tieu_de = tieu_de
        self.noi_dung = noi_dung

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Hệ thống bài tập Python nâng cao")

        self.bai_tap_list = [
            BaiTap(1, 1, "Lập trình hướng đối tượng", "Giải phương trình bậc 2"),
            # Thêm các bài tập khác cho các chương khác
        ]

        self.menu_chuong_var = tk.StringVar()
        self.menu_bai_tap_var = tk.StringVar()

        self.create_menu()

    def create_menu(self):
        menu_frame = tk.Frame(self.root, padx=10, pady=10)
        menu_frame.pack()

        # Menu chương
        chuong_label = tk.Label(menu_frame, text="Chương:")
        chuong_label.grid(row=0, column=0, padx=(0, 10))
        menu_chuong = tk.OptionMenu(menu_frame, self.menu_chuong_var, *range(1, 8))
        menu_chuong.grid(row=0, column=1, padx=(0, 10))

        # Menu bài tập
        bai_tap_label = tk.Label(menu_frame, text="Bài tập:")
        bai_tap_label.grid(row=0, column=2, padx=(0, 10))
        menu_bai_tap = tk.OptionMenu(menu_frame, self.menu_bai_tap_var, *range(1, 10))
        menu_bai_tap.grid(row=0, column=3, padx=(0, 10))

        # Nút Demo
        demo_button = tk.Button(menu_frame, text="Demo", command=self.demo)
        demo_button.grid(row=0, column=4, padx=(0, 10))

    def demo(self):
        chuong = int(self.menu_chuong_var.get())
        bai_tap = int(self.menu_bai_tap_var.get())

        bai_tap_info = self.find_bai_tap(chuong, bai_tap)

        if bai_tap_info:
            title = bai_tap_info.tieu_de
            content = bai_tap_info.noi_dung
            messagebox.showinfo(title, content)
        else:
            messagebox.showwarning("Lỗi", "Bài tập không tồn tại")

    def find_bai_tap(self, chuong, bai_tap):
        for bai_tap_info in self.bai_tap_list:
            if bai_tap_info.chuong == chuong and bai_tap_info.bai_tap == bai_tap:
                return bai_tap_info
        return None

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
