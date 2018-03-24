'''
Phương thức ẩn danh
Cú pháp: lambda [ parameter1, parameter2, ...]:
         expression
'''
import math

# Tính S = (x*x +1)^n

s = lambda x,n: math.pow(math.pow(x,2) + 1, n)
print('S = ', s(2,3))
s(3,3)