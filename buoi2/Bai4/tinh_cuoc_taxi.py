# Tính cước taxi

loai_xe        = eval(input('Loai xe (chi nhap 4 hoac 7): '))
so_km          = eval(input('So km di chuyen: '))
thoigian_cho   = eval(input('Thoi gian cho (lam tron theo phut): '))
tien_cho       = 0;
tien_di_chuyen = 0;
tien_cuoc      = 0;

#Tinh tien cho
if(thoigian_cho >= 5):
    tien_cho = (thoigian_cho - 5) * 750

if loai_xe == 4:
    # Tinh gia tien tren 1 km
    gia_tien_km = 11000
    if so_km > 0.8 and so_km < 31:
        gia_tien_km = 15300
    elif so_km >= 31:
        gia_tien_km = 12100

    # Tinh cuoc phi hien thi    
    tien_di_chuyen = gia_tien_km * so_km
    tien_cuoc      = tien_di_chuyen + tien_cho
    print('Tien cho = ',tien_cho,'; Tien di chuyen = ',tien_di_chuyen,'; Tien cuoc = ',tien_cuoc)
    
elif loai_xe ==7:
    # Tinh gia tien tren 1 km
    gia_tien_km = 12000
    if so_km > 0.8 and so_km < 31:
        gia_tien_km = 16100
    elif so_km >= 31:
        gia_tien_km = 13800

    # Tinh cuoc phi hien thi
    tien_di_chuyen = gia_tien_km * so_km
    tien_cuoc      = tien_di_chuyen + tien_cho 
    print('Tien cho = ',tien_cho,'; Tien di chuyen = ',tien_di_chuyen,'; Tien cuoc = ',tien_cuoc)
else:
    print('Loai xe khong hop le')
