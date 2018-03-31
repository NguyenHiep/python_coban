from xu_ly_file_csv import *

if __name__ == '__main__':
    if read_file_csv('thongtinkh.csv') == 1:
        print('Thong tin khach hang la:')
    else:
        print('Co loi khi doc file')
