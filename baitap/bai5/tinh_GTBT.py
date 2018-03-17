"""
Nhập số nguyên n, tính các biểu thức sau:
A = tổng các số lẻ nhỏ hơn hay bằng n
B = tổng các số chẵn nhỏ hơn hay bằng n
C = tích các số từ 1 đến n
D = tích các số chia hết cho 3 nhỏ hơn hay bằng n
E = tổng các số nguyên tố nhỏ hơn hay bằng n
"""
n = int(input("Nhập số nguyên n: "))
A,B,C,D,E = 0,0,1,1,0
i = 1

while n >= i:
    if i % 2 == 1:
        A += i
    if i% 2 == 0:
        B += i
    C  *= i
    if i %3 ==0:
        D *= i
    # E  += i
    i += 1

print("A = %i, B = %i, C = %i, D = %i, E= %i" %(A,B,C,D,E))    

    
