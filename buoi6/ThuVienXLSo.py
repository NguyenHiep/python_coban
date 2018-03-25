#from buoi6.SoNguyen import DanhSach

def themDS(danhSach):
    print("Nhap -1 de dung lai!")
    number = 1
    while(number != -1):
        number = eval(input("Nhap phan tu: \t"))
        if(number != -1):
            danhSach.append(number)

def inDanhSach(danhSach):
    ds = ''
    for item in danhSach:
        ds += str(item) + ' '
    print(ds)

def tongSoChan(danhSach):
    tong_chan = 0
    for item in danhSach:
        if item % 2 == 0:
            tong_chan += item
    print('Tong cac so chang: ', tong_chan)

def tongSoLe(danhSach):
    tong_le = 0
    for item in danhSach:
        if item % 2 != 0:
            tong_le += item
    print('Tong cac so le: ', tong_le)

def kiemtraNguyenTo(so):
    if so < 2:
        return False
    flag = True

    for i in range(2, so):
        if so % i == 0:
            flag = False
            break
    return flag

def danhSachNguyenTo(danhSach):
    ds = ''
    for item in danhSach:
        if kiemtraNguyenTo(item) == True:
            ds += str(item) + ' '
    print(ds)
    