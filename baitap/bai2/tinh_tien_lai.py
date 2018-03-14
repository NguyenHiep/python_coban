laisuat_motnam = eval(input("Nhập lãi suất 1 năm (%): \n"))
so_tien_gui    = eval(input("Số tiền gửi: \n"))
so_thang_gui   = eval(input("Số tháng gửi: \n"))
tien_lai       = (so_tien_gui*so_thang_gui)*(laisuat_motnam/100/12)
tong_tien      = so_tien_gui + tien_lai

print("Tiền lãi = %.1f"%tien_lai)
print("Tiền vốn + lãi = %d + %d = %d"%(so_tien_gui,tien_lai,tong_tien))