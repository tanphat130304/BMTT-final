from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()

while True:
    print("\nCHUONG TRINH QUAN LY SINH VIEN")
    print("*************************MENU**************************")
    print("**  1. Them sinh vien.                               **")
    print("**  2. Cap nhat thong tin sinh vien boi ID.          **")
    print("**  3. Xoa sinh vien boi ID.                         **")
    print("**  4. Tim kiem sinh vien theo ten.                  **")
    print("**  5. Sap xep sinh vien theo diem trung binh (GPA). **")
    print("**  6. Sap xep sinh vien theo ten chuyen nganh.      **")
    print("**  7. Hien thi danh sach sinh vien.                 **")
    print("**  0. Thoat                                         **")
    print("*************************MENU**************************")

    try:
        key = int(input("Nhap tuy chon (0-7): "))
        if key == 1:
            print("\n1. Them sinh vien.")
            qlsv.nhapSinhVien()
            print("\nThem sinh vien thanh cong!")
        elif key == 2:
            if qlsv.soLuongSinhVien() > 0:
                print("\n2. Cap nhat thong tin sinh vien.")
                try:
                    ID = int(input("Nhap ID sinh vien (>= 1): "))
                    if ID < 1:
                        raise ValueError("ID phai >= 1.")
                    qlsv.updateSinhVien(ID)
                except ValueError as e:
                    print("\nLoi: ", e)
            else:
                print("\nDanh sach sinh vien trong!")
        elif key == 3:
            if qlsv.soLuongSinhVien() > 0:
                print("\n3. Xoa sinh vien.")
                try:
                    ID = int(input("Nhap ID sinh vien (>= 1): "))
                    if ID < 1:
                        raise ValueError("ID phai >= 1.")
                    if qlsv.deleteById(ID):
                        print("\nSinh vien co ID = ", ID, " da bi xoa.")
                    else:
                        print("\nSinh vien co ID = ", ID, " khong ton tai.")
                except ValueError as e:
                    print("\nLoi: ", e)
            else:
                print("\nDanh sach sinh vien trong!")
        elif key == 4:
            if qlsv.soLuongSinhVien() > 0:
                print("\n4. Tim kiem sinh vien theo ten.")
                name = input("Nhap ten de tim kiem: ")
                searchResult = qlsv.findByName(name)
                qlsv.showSinhVien(searchResult)
            else:
                print("\nDanh sach sinh vien trong!")
        elif key == 5:
            if qlsv.soLuongSinhVien() > 0:
                print("\n5. Sap xep sinh vien theo diem trung binh.")
                qlsv.sortByDiemTB()
                qlsv.showSinhVien(qlsv.getListSinhVien())
            else:
                print("\nDanh sach sinh vien trong!")
        elif key == 6:
            if qlsv.soLuongSinhVien() > 0:
                print("\n6. Sap xep sinh vien theo ten chuyen nganh.")
                qlsv.sortByName()
                qlsv.showSinhVien(qlsv.getListSinhVien())
            else:
                print("\nDanh sach sinh vien trong!")
        elif key == 7:
            if qlsv.soLuongSinhVien() > 0:
                print("\n7. Hien thi danh sach sinh vien.")
                qlsv.showSinhVien(qlsv.getListSinhVien())
            else:
                print("\nDanh sach sinh vien trong!")
        elif key == 0:
            print("\nBan da chon thoat chuong trinh!")
            break
        else:
            print("\nKhong co chuc nang nay! Vui long chon so tu 0 den 7.")
            print("\nHay chon chuc nang trong hop menu.")
    except ValueError:
        print("\nLoi: Vui long nhap mot so nguyen!")