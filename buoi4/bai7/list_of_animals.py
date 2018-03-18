"""list_ani = ['ant','bear','cat','dog','elephant','fish','goat','hippo']"""

list_animal = []
animal_name = ''
print("Nhap -1 de dung lai!")
while(animal_name != '-1'):
        animal_name = str(input("Nhap ten con vat: "))
        if animal_name != '-1':
            list_animal.append(animal_name)

ds_name = ""
for animal in list_animal:
    ds_name += animal + " "

print("Danh sach cac con vat vua nhap vao: \t", ds_name)

print("So luong con vat: ", len(list_animal))

find_name = str(input("Nhap ten con vat ban muon tim: \t"))

if find_name in list_animal:
    print("%s co trong danh sach con vat"%find_name)
else:
    print("%s khong co trong danh sach"%find_name)