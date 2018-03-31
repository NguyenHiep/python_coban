import os


def doc_file(path):
    f       = open(path, 'r')
    noidung = f.read()
    f.close()
    return noidung

def ghi_file(path, mode, noidung):
    try:
        kq = 1
        f  = open(path, mode)
        f.write(noidung)
        f.write('\n')
    except Exception as ex:
            kq = -1
    finally:
        f.close()
        return kq

def them_noi_dung(path):
    try:
        kq = 1
        f  = open(path,'a')
        tt = 1
        while tt == 1:
            noidung = str(input('Nhap noi dung can them \t'))
            f.write(noidung)
            f.write('\n') # Them dong nay de text them vo xuong hang
            tt = int(input('Tiep tuc khong (1) \t'))
    except Exception as ex:
        kq = -1
    finally:
        f.close()
        return kq

def doi_ten_file(file_current, file_new):
    try:
        kq = 1
        os.rename(file_current, file_new)
    except Exception as ex:
        kq = -1
    finally:
        return kq


def xoa_file(file_name):
    try:
        kq = 1
        os.remove(file_name)
    except Exception as ex:
        kq = -1
    finally:
        return kq


def thong_ke(path):
    
    try:
        kq = 1
        so_tu = 0
        so_dong = 0
        so_ky_tu = 0
        f = open(path, 'r')
        for dong in f :
            so_dong +=1
            arrDong = dong.split()
            print(arrDong)
        
    except Exception as ex:
        kq = -1
    finally:
        return kq
    

