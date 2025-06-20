from SinhVien import SinhVien

class QuanLySinhVien:
    listSinhVien = []

    def generateID(self):
        maxID = 1
        if (self.soLuongSinhVien() > 0):
            maxID = self.listSinhVien[0]._id
            for sv in self.listSinhVien:
                if (maxID < sv._id):
                    maxID = sv._id
            maxID = maxID + 1
        return maxID

    def soLuongSinhVien(self):
        return self.listSinhVien.__len__()

    def nhapSinhVien(self):
        svID = self.generateID()
        name = input("Nhap ten sinh vien: ").strip()
        if not name:
            print("Loi: Ten sinh vien khong duoc de trong!")
            return
        sex = input("Nhap gioi tinh sinh vien: ").strip()
        if not sex:
            print("Loi: Gioi tinh khong duoc de trong!")
            return
        major = input("Nhap chuyen nganh cua sinh vien: ").strip()
        if not major:
            print("Loi: Chuyen nganh khong duoc de trong!")
            return
        try:
            diemTB = float(input("Nhap diem cua sinh vien: "))
            if diemTB < 0 or diemTB > 10:
                raise ValueError("Diem TB phai tu 0 den 10.")
            sv = SinhVien(svID, name, sex, major, diemTB)
            self.listSinhVien.append(sv)
        except ValueError as e:
            print("Loi: ", e)

    def updateSinhVien(self, ID):
        sv = self.findByID(ID)
        if (sv != None):
            name = input("Nhap ten sinh vien: ").strip()
            if not name:
                print("Loi: Ten sinh vien khong duoc de trong!")
                return
            sex = input("Nhap gioi tinh sinh vien: ").strip()
            if not sex:
                print("Loi: Gioi tinh khong duoc de trong!")
                return
            major = input("Nhap chuyen nganh cua sinh vien: ").strip()
            if not major:
                print("Loi: Chuyen nganh khong duoc de trong!")
                return
            try:
                diemTB = float(input("Nhap diem cua sinh vien: "))
                if diemTB < 0 or diemTB > 10:
                    raise ValueError("Diem TB phai tu 0 den 10.")
                sv._name = name
                sv._sex = sex
                sv._major = major
                sv._diemTB = diemTB
                sv.capNhatHocLuc()
                print("Cap nhat thong tin sinh vien thanh cong!")
            except ValueError as e:
                print("Loi: ", e)
        else:
            print("Sinh vien co ID = {} khong ton tai.".format(ID))

    def sortByID(self):
        self.listSinhVien.sort(key=lambda x: x._id, reverse=False)
        print("Da sap xep danh sach sinh vien theo ID.")

    def sortByMajor(self):  # Đổi tên để rõ ràng
        self.listSinhVien.sort(key=lambda x: x._major, reverse=False)
        print("Da sap xep danh sach sinh vien theo chuyen nganh.")

    def sortByDiemTB(self):
        self.listSinhVien.sort(key=lambda x: x._diemTB, reverse=False)
        print("Da sap xep danh sach sinh vien theo diem trung binh.")

    def findByID(self, ID):
        if ID < 1:
            print("Loi: ID phai >= 1.")
            return None
        searchResult = None
        if (self.soLuongSinhVien() > 0):
            for sv in self.listSinhVien:
                if (sv._id == ID):
                    searchResult = sv
                    break
        return searchResult

    def findByName(self, keyword):
        listSV = []
        if (self.soLuongSinhVien() > 0):
            for sv in self.listSinhVien:
                if (keyword.upper() in sv._name.upper()):
                    listSV.append(sv)
        if not listSV:
            print("Khong tim thay sinh vien nao co ten chua tu khoa '{}'.".format(keyword))
        return listSV

    def deleteById(self, ID):
        if ID < 1:
            print("Loi: ID phai >= 1.")
            return False
        isDeleted = False
        sv = self.findByID(ID)
        if (sv != None):
            self.listSinhVien.remove(sv)
            isDeleted = True
        return isDeleted

    def showSinhVien(self, listSV):
        print("\n" + "-"*60)
        print("{:<8} {:<18} {:<8} {:<8} {:<8} {:<8}".format("ID", "Name", "Sex", "Major", "Diem TB", "Hoc Luc"))
        print("-"*60)
        if (listSV.__len__() > 0):
            for sv in listSV:
                print("{:<8} {:<18} {:<8} {:<8} {:<8} {:<8}".format(sv._id, sv._name, sv._sex, sv._major, sv._diemTB, sv._hocLuc))
        else:
            print("Danh sach sinh vien trong!")
        print("-"*60 + "\n")

    def getListSinhVien(self):
        return self.listSinhVien