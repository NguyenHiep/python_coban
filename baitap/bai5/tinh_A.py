n = int(input("Nhập n: "))
x = eval(input("Nhập x: "))

#A = (x^2 + x +1)^n + (x^2 - x + 1)^n
A = (x*x + x + 1)**n + (x**x - x + 1)**n
print("A = %i"%A)
 