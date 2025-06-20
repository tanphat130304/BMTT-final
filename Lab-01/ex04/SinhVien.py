class SinhVien:
    def __init__(self, id, name, sex, major, diemTB):
        # Kiểm tra tính hợp lệ của id
        if id < 1:
            raise ValueError("ID phai >= 1.")
        self._id = id

        # Kiểm tra tính hợp lệ của name, sex, major
        if not name or name.isspace():
            raise ValueError("Ten sinh vien khong duoc de trong.")
        self._name = name.strip()

        if not sex or sex.isspace():
            raise ValueError("Gioi tinh khong duoc de trong.")
        self._sex = sex.strip()

        if not major or major.isspace():
            raise ValueError("Chuyen nganh khong duoc de trong.")
        self._major = major.strip()

        # Kiểm tra tính hợp lệ của diemTB
        if not isinstance(diemTB, (int, float)):
            raise ValueError("Diem TB phai la so.")
        if diemTB < 0 or diemTB > 10:
            raise ValueError("Diem TB phai tu 0 den 10.")
        self._diemTB = diemTB

        self._hocLuc = self._tinhHocLuc()

    def _tinhHocLuc(self):
        if self._diemTB >= 8:
            return "Gioi"
        elif self._diemTB >= 6.5:
            return "Kha"
        elif self._diemTB >= 5:
            return "Trung binh"
        else:
            return "Yeu"

    def capNhatHocLuc(self):
        self._hocLuc = self._tinhHocLuc()
        print(f"Hoc luc cua sinh vien {self._name} da duoc cap nhat: {self._hocLuc}")

    # Getter methods
    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_sex(self):
        return self._sex

    def get_major(self):
        return self._major

    def get_diemTB(self):
        return self._diemTB

    def get_hocLuc(self):
        return self._hocLuc