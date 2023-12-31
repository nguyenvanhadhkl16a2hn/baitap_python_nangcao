# Nhập số nguyên N từ bàn phím
N = int(input("Nhập số nguyên N: "))

# Khởi tạo danh sách ước số
uoc_so = []

# Duyệt qua các số từ 1 đến N và kiểm tra xem số đó có phải là ước của N hay không
for i in range(1, N+1):
    if N % i == 0:
        uoc_so.append(i)

# In ra danh sách ước số
print("Các ước số của", N, "là:", uoc_so)
