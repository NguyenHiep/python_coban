list_numbers = []

print("Nhap -1 de dung lai!")
number = 1
while(number != -1):
    number = eval(input("Nhap phan tu: \t"))
    if(number != -1):
        list_numbers.append(number)

print("List ban vua nhap: ", list_numbers)

find_number = eval(input("Nhap gia tri can tim: \t"))
sum = 0
for num in list_numbers:
    sum += num
print("Tong cac gia tri trong list:", sum)

count = list_numbers.count(find_number)
if count > 0:
    print("%d co trong list va xuat hien %d lan"%(find_number, count))
else:
    print("%d khong co trong list")

gt_max = max(list_numbers)
list_max = []
if find_number > gt_max:
    print("%d lon hon tat ca cac so trong list")
else:
    for num in list_numbers:
        if find_number < num:
            list_max.append(num)
    print("%d khong lon hon tat ca cac so trong list"%find_number)
    print("Cac so lon hon %d trong list: %s "%(find_number, list_max))
            
            
        
