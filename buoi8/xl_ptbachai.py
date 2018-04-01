
import math
import json
import os

def NhapDSPTBacHai(path):
    try:
        flag = 1
        dsPT = []
        n = 0
        while n <= 0:
            n = int(input('Ban muon nhap bao nhieu phuong trinh'))
        for i in range(n):
            a,b,c = eval(input('Nhap a,b,c: \t'))
            pt = {'a': a, 'b': b, 'c': c}
            dsPT.append(pt)
        # Luu vao file
        f = open(path, 'w')
        for pt in dsPT:
            f.write(str(pt))
        f.close()

    except Exception as ex:
        flag = -1
    finally:
        return flag

def InDanhSach(path):
    try:
        f = open(path)
        for pt in f.read():
            print(pt)
        
    except Exception as ex:
        print('Cos loi')
    finally:
        pass
