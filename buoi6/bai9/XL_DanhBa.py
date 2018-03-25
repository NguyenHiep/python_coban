#Thu vien function xu ly danh ba

def themDanhBa(DanhBa):
    tt = eval(input('Ban muon nhap bao nhieu nguoi: '))
    # Add item 
    for i in range(tt):
        name  = str(input('Nhap ten thanh vien: '))
        phone = str(input('Nhap so dien thoai: '))
        DanhBa[name] = phone

def inDanhBa(DanhBa):
    # In danh sach    
    for key, value in DanhBa.items():
        print(key,'<--->', value)

def timkiem(DanhBa, ten):
    phone = DanhBa.get(ten)
    if phone != None:
        print(ten,'---', phone)
    else:
        print('Khong tim thay trong danh ba')

def CapNhatDanhBa(DanhBa):
    name = str(input('Nhap ten thanh vien:'))
    phone = str(input('Nhap so dien thoai:'))
    DanhBa[name] = phone

def XoaThanhVien(DanhBa,ten):
    phone = DanhBa.get(ten)
    if phone != None:
            ## code
            pass
    else:
        print('Khong tim thay thanh vien naytrong danh ba')

