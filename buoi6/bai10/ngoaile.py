def thuonghaiso(x,y):
    assert(y!=0),'Không thể chia cho 0'
    return x/y
try:
    x = eval(input('Nhap x = '))
    y = eval(input('Nhap y = '))
    thuong = thuonghaiso(x,y)
    print('%.2f'%thuong)
except Exception as e:
    print('Co loi xay ra: ', e)