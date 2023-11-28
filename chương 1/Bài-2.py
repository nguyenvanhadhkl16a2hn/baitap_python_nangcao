class Thi_sinh:
        def __init__(self,ho_ten,diem_Toan,diem_Ly,diem_Hoa,diem_Tb):
            self._ho_ten = ho_ten
            self._diem_Toan = diem_Toan
            self._diem_Ly = diem_Ly
            self._diem_Hoa = diem_Hoa
            self._diem_Tb = diem_Tb
class manager_Thi_sinh:
    list_Thi_sinh = []
    list_Thi_sinh_20 = []
    def so_luong_Thi_sinh(self):
        return self.list_Thi_sinh.__len__()
    def add_Thi_sinh(self):
        name = input("nhập họ và tên: ")
        diem_toan = float(input("nhập điểm môn toán: "))
        diem_ly = float(input("nhập điểm môn lý: "))
        diem_hoa = float(input("nhập điểm môn hóa: "))
        diem_tb = diem_toan + diem_ly + diem_hoa
        thisinh = Thi_sinh(name, diem_toan, diem_ly, diem_hoa, diem_tb)
        self.list_Thi_sinh.append(thisinh)
        if diem_tb >= 20:
            self.list_Thi_sinh_20.append(thisinh)
    def sap_xep(self):
        self.list_Thi_sinh_20.sort(key = lambda x: x._diem_Tb, reverse=True)
        self.list_Thi_sinh.sort(key = lambda x: x._diem_Tb, reverse=True)
    def show_thi_sinh(self):
        print("{:<8} {:<18} {:<8} {:<8}{:<8}".format("Name", "điểm toán", "điểm lý", "điểm hóa",'điểm trung bình'))
        if (self.list_Thi_sinh.__len__() > 0):
            for sv in self.list_Thi_sinh:
                print("{:<8} {:<18} {:<8} {:<8}{:<8}".format(sv._ho_ten, sv._diem_Toan, sv._diem_Ly, sv._diem_Hoa, sv._diem_Tb))
        print("\n")
    def show_thi_sinh_20(self):
        print("{:<8} {:<18} {:<8} {:<8}{:<8}".format("Name", "điểm toán", "điểm lý", "điểm hóa",'điểm trung bình'))
        if (self.list_Thi_sinh_20.__len__() > 0):
            for sv in self.list_Thi_sinh_20:
                print("{:<8} {:<18} {:<8} {:<8}{:<8}".format(sv._ho_ten, sv._diem_Toan, sv._diem_Ly, sv._diem_Hoa, sv._diem_Tb))
        print("\n")
def main():
    managerthisinh = manager_Thi_sinh()
    while (1==1):
        print("hãy nhấn các số dưới kia để thực hiện lệnh")
        print("1: thêm thí sinh: ")
        print("2: danh sách thí sinh : ")
        print("3: sắp xếp các thí sinh có điểm từ cao xuống thấp: ")
        print("4: danh sách các thí sinh trúng tuyển từ cao xuống thấp")
        print("0: thoát")
        key = input("nhập tùy chọn: ")
        if key == "1":
            managerthisinh.add_Thi_sinh()
        if key == "2":
            managerthisinh.show_thi_sinh()
        if key == '3':
            managerthisinh.sap_xep()
        if key == '4':
            managerthisinh.show_thi_sinh_20()
        if key == "0":
            break
if __name__ == "__main__":
    main()