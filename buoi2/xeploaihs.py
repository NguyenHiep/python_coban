diem_trung_binh = eval(input('Vui long nhap diem trung binh: '))
if diem_trung_binh >=0 and diem_trung_binh <=10:
    if diem_trung_binh < 5:
        print("Yeu/Kem")
    elif diem_trung_binh < 6:
        print('Trung Binh')
    elif diem_trung_binh < 7:
        print('TB Kha')
    elif diem_trung_binh < 8:
        print('Kha')
    elif diem_trung_binh < 9:
        print('Gioi')
    else:
        print('Xuat sac')        
        
else:
    print('Diem nhap vao khong hop le')