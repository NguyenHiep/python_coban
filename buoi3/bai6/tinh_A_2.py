n = int(input("Nhap n: "))
x = eval(input("Nhap x: "))
S = pow((pow(x,2) + x + 1), n) + pow((pow(x,2) - x + 1), n)

print("Tong S = ", S)