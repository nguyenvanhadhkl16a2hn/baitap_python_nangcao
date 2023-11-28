class Hinh_chu_nhat:
    def __init__(self, a,b):
        self.a = a
        self.b = b
    def Print(self):
        return self.a, self.b
    def S_hinh_chu_nhat(self):
        return self.a * self.b
    
    def V_hinh_chu_nhat(self):
        return 2 * (self.a + self.b)
print("chiều dài 2 cạnh của hình chữ nhật là: ")
Hinh_chu_nhat = Hinh_chu_nhat(5, 3)
S = Hinh_chu_nhat.S_hinh_chu_nhat()  
V = Hinh_chu_nhat.V_hinh_chu_nhat()  
Print = Hinh_chu_nhat.Print()
print("độ dài 2 cạnh của hình chữ nhật lần lượt là: ",Print)
print("diện tích hình chữ nhật là: ", S)
print("chu vi hình chữ nhật là: ", V)