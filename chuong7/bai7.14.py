import tkinter as tk

class TaxiCalculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Tính cước taxi")

        self.distance_label = tk.Label(master, text="Khoảng cách (km):")
        self.distance_label.grid(row=0, column=0, padx=10, pady=10)

        self.distance_entry = tk.Entry(master)
        self.distance_entry.grid(row=0, column=1, padx=10, pady=10)

        self.calculate_button = tk.Button(master, text="Tính cước", command=self.calculate_fare)
        self.calculate_button.grid(row=1, column=0, columnspan=2, pady=10)

        self.result_label = tk.Label(master, text="")
        self.result_label.grid(row=2, column=0, columnspan=2, pady=10)

    def calculate_fare(self):
        try:
            distance = float(self.distance_entry.get())
            fare = self.calculate_taxi_fare(distance)
            self.result_label.config(text=f"Cước phí: {fare:.2f} đồng")
        except ValueError:
            self.result_label.config(text="Nhập khoảng cách là một số")

    def calculate_taxi_fare(self, distance):
        base_fee = 12000  # Giá mở cửa
        distance_limit = 0.8  # Giới hạn khoảng cách miễn phí
        rate_per_km = 15000  # Giá cước cho mỗi km vượt quá giới hạn miễn phí

        if distance <= distance_limit:
            return base_fee
        else:
            extra_distance = distance - distance_limit
            extra_fare = extra_distance * rate_per_km
            total_fare = base_fee + extra_fare
            return total_fare

if __name__ == "__main__":
    root = tk.Tk()
    app = TaxiCalculator(root)
    root.mainloop()
