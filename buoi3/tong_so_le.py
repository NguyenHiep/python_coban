n = int(input("n = "))
tong = 0

for i in range(1, n +1):
    if i % 2 == 0:
        continue
    tong += i 
print("Tong  = %d"%tong)