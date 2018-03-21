ds_KhachHang = {"Jonhny":"0908421534","Tenu":"0908414356","Jack":"0942136581","Tony":"0983451267"}

tt = 1
while tt == 1 :
    print("Ban muon lam gi? 1: Xem danh ba, 2: Tim kiem, 3: Them moi")
    chon = eval(input(''))
    
    if chon == 1:
        print("Danh sach khach hang")
        for key, value in ds_KhachHang.items():
            print (key,'---------------',value)
    elif chon == 2:
        print("Tim kiem khach hang:")
        find_name = str(input("Nhap ten khach hang: "))
        if ds_KhachHang.get(find_name, "None") != "None":
            print(find_name, ds_KhachHang.get(find_name))
        else:
            print("Khong tim thay khach hang")

    elif chon ==3:
        name  = str(input("Nhap ten khach hang: "))
        phone = str(input("so dien thoai la: "))
        ds_KhachHang[name] = phone
    else:
        print("Chi dc chon 1,2,3")
    tt = eval(input("Chon 1 de tiep tuc, 0 de dung lai!"))
