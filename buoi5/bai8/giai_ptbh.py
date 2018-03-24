import math

def giaiPTBacHai(a,b,c):
    ketqua = ''
    if a == 0:
        if b == 0 and c != 0 :
            return "Phuong trinh vo nghiem"
        elif b == 0 and c == 0 :
            return "Phuong trinh vo so nghiem"
        else:
            return "Phuong trinh co nghiem x = " + str(-c/b)
    else:
        delta = b*b - 4*a*c
        if delta < 0:
            ketqua = "Phuong trinh vo nghiem"
        elif delta == 0:
            ketqua = "Phuong trinh co nghiem kep x1 = x2 = " + str(-b /(2*a))
        else:
            ketqua = "Phuong trinh co 2 nghiem phan biet: x1 = " + str((-b + math.sqrt(delta)) / (2*a)) + "x2 = " +  str((-b - math.sqrt(delta)) / (2*a))
    return ketqua
if __name__ == '__main__': # File khac import khong su dung duoc doan code trong if
    a = eval(input("Nhap so nguyen a:"))
    b = eval(input("Nhap so nguyen b:"))
    c = eval(input("Nhap so nguyen c:"))
    nghiem = giaiPTBacHai(a,b,c)
    print(nghiem)
