class Loi_nhap_lieu(ValueError):
    def __init__(self, args):
        self.args = args
    
try:
    x = 1
    if type(x) != int:
        raise Loi_nhap_lieu('Du lieu nhap phai la so')
    
except Loi_nhap_lieu as ex:
    loi = ''
    for i in ex.args:
        loi += str(i)
    print('Loi:', loi)
else:
    print('Khong co loi')