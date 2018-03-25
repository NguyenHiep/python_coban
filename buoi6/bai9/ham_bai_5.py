# Function trong bai tap 5
import math

def count_down():
    songuyen = eval(input('Nhap so nguyen n: \t'))
    while songuyen > 0:
        print(songuyen,'\n')
        songuyen -=1
    else:
        print('Start!!!')

def tinh_S():
    n = eval(input('Nhap so nguyen n: \t'))
    x = eval(input('Nhap so mu x: \t'))
    S = pow(pow(x,2),n)
    print('S = (x*x + 1)^n = ', S)

def tinh_A():
     n = eval(input('Nhap so nguyen n: \t'))
     x = eval(input('Nhap so mu x: \t'))
     A = pow(pow(x,2) + x + 1, n) + pow(pow(x,2) - x + 1, n)
     print('A = (x^2 + x + 1)^n  + (x^2 - x + 1)^n= ', A)

def kiemtraNguyenTo(so):
    if so < 2:
        return False
    flag = True

    for i in range(2, so):
        if so % i == 0:
            flag = False
            break
    return flag

def tongSoChan(so):
    tong_chan = 0
    for i in range(1,so):
        if i % 2 == 0:
            tong_chan += i
    print('Tong cac so chang: ', tong_chan)

def tongSoLe(so):
    tong_le = 0
    for i in range(1,so):
        if i % 2 != 0:
            tong_le += i
    print('Tong cac so le: ', tong_le)

def tichSoN(so):
    tich = 1
    for i in range(1,so):
        tich *= i
    print('Tich cac so: ', tich)

def tichSoChiaHetCho3(so):
    tich = 1
    for i in range(1,so):
        if i % 3 == 0:
            tich *= i
    print('Tich cac so chia het cho 3: ', tich)

def tongNguyenTo(so):
    tong = 0
    for i in range(1,so):
        if kiemtraNguyenTo(i) == True:
            tong += i
    print('Tong cac nguyen to la: ', tong)

def dsSoNguyen(so):
    ds = ''
    for i in range(1, so):
        ds += str(i) + ' '
    print('Danh sach co nguyen < %d: ' %so)
    print(ds)

def dsSoNguyenTo(so):
    ds = ''
    for i in range(1, so):
        if kiemtraNguyenTo(i) == True:
            ds += str(i) + ' '
    print('Danh sach co nguyen to: ')
    print(ds)
