import math

a,b,c = eval(input("Nhap a,b,c: "))

if a == 0:
    if b == 0 and c != 0:
        print("Phuong trinh vo nghiem")
    elif b == 0 and c == 0:
        print("Phuong trinh vo so nghiem")    
    else:
        print("Phuong trinh co nghiem x = ", -c/b)
else:
    delta = pow(b,2) - 4*a*c
    if delta < 0:
        print("Phuong trinh vo nghiem")
    elif delta == 0:
        print("Phuong trinh co nghiep kep: x1 = x1 = ", -b/(2*a))
    else:
        print("Phuong trinh co 2 nghiem phan biet: x1 =", (-b + math.sqrt(delta)) / (2*a), "x2 = ", (-b - math.sqrt(delta)) / (2*a))    
        
