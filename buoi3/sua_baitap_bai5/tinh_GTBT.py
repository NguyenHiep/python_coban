n = int(input("Nhap so nguyen n: "))
tong_le   = 0
tong_chan = 0
tich_n      = 1
tich_chia_het_cho_3 = 1
tong_nguyen_to      = 0

for i in range(1, n+1):
    if n % 2 == 1:
        tong_le += i
    """if n % 2 == 0:
        tong_chan += i
    tich_n *= i
    if n % 3 == 0:
        tich_chia_het_cho_3 *= i"""
    
print("A =",tong_le)
print("B = ", tong_chan)
print("C = ", tich_n)
print("D = ", tich_chia_het_cho_3)
print("E = ", tong_nguyen_to)