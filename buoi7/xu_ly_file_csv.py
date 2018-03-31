import csv

def read_file_csv(path):
    try:
        kq = 1
        f = open(path)
        ds_khachhang = csv.reader(f)
        for khachhang in ds_khachhang:
            print(khachhang)
    except Exception as ex:
        kq = -1
    finally:
        f.close()
        return kq
    
    
    