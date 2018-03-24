'''
Nhập n, x tính giá trị các biểu thức sau:
S = (x^2 + 1)^nn
A = (x^2 + x + 1)^n + (x^2 - x + 1)^n
Kiểm tra x có phải là số nguyên tố không    
'''
import math

def tinh_S(n,x):
    return pow(pow(x,2) + 1,n)

def tinh_A(n,x):
    return pow(pow(x,2) + x + 1, n) + pow(pow(x,2) - x +1 ,n)

def kiem_tra_so_nguyen_to(x):
    is_nguyento = True
    if x < 2:
        is_nguyento = False
    else:    
        for i in range(2, x):
            if x % i == 0:
                is_nguyento = False
                break
    return is_nguyento

if __name__ == '__main__':
    x = eval(input('Nhap so nguyen x = '))
    n = eval(input('Nhap so nguyen n = '))
    print("Tong S = ",tinh_S(n,x))
    print("Tong A = ", tinh_A(n,x))
    if kiem_tra_so_nguyen_to(x) == True:
        print("%d la so nguyen to"%x)
    else:
        print("%d khong la so nguyen to"%x)

    if kiem_tra_so_nguyen_to(n) == True:
        print("%d la so nguyen to"%n)
    else:
        print("%d khong la so nguyen to"%n)   