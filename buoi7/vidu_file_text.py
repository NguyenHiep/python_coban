from xuly_file_text import *

if __name__ == '__main__':

    tt = 1
    while tt == 1:
        print('1. Tao file moi')
        print('2. Mo file')
        print('3. Them noi dung')
        print('4. Doi ten file')
        print('5. Xoa file')
        chon = int(input('Chon chuc nang: \t'))
        if chon == 1:
            ten     = str(input('Cho biet ten file: '))
            noidung = str(input('Cho biet noi dung ghi: '))
            ghi_file(ten,'w', noidung)
        elif chon == 2:
            ten = str(input('Cho biet ten file: '))
            print(doc_file(ten))
        elif chon == 3:
            ten = str(input('Cho biet ten file: '))
            them_noi_dung(ten)
        elif chon == 4:
            ten     = str(input('Nhap ten file can doi: '))
            ten_moi = str(input('Ten file moi: '))
            if doi_ten_file(ten, ten_moi) == 1:
                print('Doi ten thanh khong')
            else:
                print('Doi ten khong thanh cong')
        elif chon == 5:
            ten = str(input('Nhap ten file muon xoa: '))
            if xoa_file(ten) == 1:
                  print('Xoa file thanh khong')
            else:
                print('Xoa file khong thanh cong')
                
        tt = int(input('Ban muon tiep tuc (1): '))
