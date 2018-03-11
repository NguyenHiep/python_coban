a,b,c,d = eval(input('Nhap so nguyen a,b,c,d: '))

min = a
max = a

#Tim min 
if(min>b):
    min = b
if(min > c):
    min = c
if(min > d):
    min = d

#Tim max
if(max < b):
    max = b
if(max < c):
    max = c
if(max < d):
    max = d

print('a = ',a,'; b = ',b,'; c = ',c,'; d = ',d)
print('max = ', max, '; min = ', min)
 