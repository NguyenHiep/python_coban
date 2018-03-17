"""
Nhap va so nguyen n va mot so thuc x. Tinh va in ra ket qua bieu thuc sau:
A = (x^2 + x + 1)^n + (x^2 - x +1)^n

"""
n    = int(input("Nhap n: "))
x    = eval(input("Nhap x: "))
S    = 1
S2   = 1
for i in range(1, n+1):
    S  *= (x*x + x + 1)
    S2 *= (x*x - x + 1)
Tong = S + S2
print(Tong)