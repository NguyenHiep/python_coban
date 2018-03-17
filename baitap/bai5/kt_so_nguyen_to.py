x = eval(input("Nhập X: "))

i = 2
is_nguyen_to = 1

if(x < 2):
    is_nguyen_to = 0

while(x > i):
    if(x % i == 0):
        is_nguyen_to = 0
        break
    i += 1

if is_nguyen_to == 1:
    print("%i là số nguyên tố"%x)
else:
   print("%i không là số nguyên tố"%x)     
    

