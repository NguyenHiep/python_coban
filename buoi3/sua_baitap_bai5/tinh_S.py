"""
Nhap va so nguyen n va mot so thuc x. Tinh va in ra ket qua sau:
S = (x^2 + 1)^n
"""
n = int(input("Nhap n: "))
x = eval(input("Nhap x: "))
S = 1
for i in range(1, n+1):
    S *=(x*x +1)
print(S)