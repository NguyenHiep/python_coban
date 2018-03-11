# Tìm giá trị tuyệt đối
x = int(input('Nhap vao so nguyen: '))
abs_x = x

if x < 0:
    abs_x = -x
print('|%i| = %i' %(x, abs_x))