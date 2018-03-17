"""
===========================================================
Nhap va chuoi s, chuoi s_sub, s_find, s_replace
+ in chuoi s
+ Loai bo khoang trang o dau va cuoi chuoi
+ In chuoi voi ky tu dau chuoi viet hoa
+ Dem va in ra so lan chuoi con s_sub xuat hien trong chuoi s
+ Tim kiem s_find trong s va thay the bang s_replace, in chuoi sau khi tim kiem va thay the
===========================================================
"""
s         = str(input("Nhap chuoi s: \n"))
s_sub     = str(input("Nhap chuoi con s_sub: \n"))
s_find    = str(input("Nhap chuoi tim s_find: \n"))
s_replace = str(input("Nhap chuoi thay the s_replace:"))

print("Chuoi s sau khi loai bo khoang trang dau va cuoi chuoi: ", s.strip())
print("Chuoi viet hoa ky tu dau: ", s.capitalize())
print("So la chuoi s_sub xuat hien trong chuoi s: ", s.count(s_sub))
print("Chuoi s sau khi tim tiem va thay the: ", s.replace(s_find, s_replace))


