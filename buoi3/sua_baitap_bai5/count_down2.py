"""
Nhap so nguyen n va
In ra ma hinh ket qua nhu sau:
+ n = 3: 3 2 1
+ n = 7: 7 6 5 4 3 2 1
"""
n = int(input('Nhap vao so nguyen n:'))
chuoi = 'n = '+ str(n) + ': '
while n > 0:
    chuoi += str(n) + ' '
    n -= 1
print(chuoi)