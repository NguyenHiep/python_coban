so_nguyen = int(input('Vui long nhap so nguyen: '))
i = 1
tong = 0
while(i <= so_nguyen):
    if(i % 2 == 0):
        tong += i
    i += 1
print('Tong cac so chan tu %i den %i la: %i'%(i,so_nguyen,tong))