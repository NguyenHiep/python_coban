n = int(input("Nhap n: "))
flag = 1

if n >= 2:
    for i in range(2,n):
        if n % i == 0:
            flag = 0
            break
    if flag == 1:
        print("%d la so nguyen to" %n)
    else:
        print("%d khong la so nguyen to" %n)
else:
    print("%d khong la so nguyen to")