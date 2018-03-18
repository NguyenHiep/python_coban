list_1 = ["a", "b", "c", "d"]

list_2 = []
temp = 1;

while temp != -1:
    temp = eval(input("Nhap so phan tu cho list2:"))
    if temp != -1:
        list_2.append(temp)
        
print("List 1 co : ", len(list_1), "phan tu")
print("List 2 co : ", len(list_2), "phan tu")

print("=========================== LIST 1 ===========================")
# Duyet danh sach cach 1 theo index (chi muc)
for i in range(len(list_1)):
    print(list_1[i])

print("=========================== LIST 2 ===========================")
# Duyet danh sach cach 2
for item in list_2:
    print(item)