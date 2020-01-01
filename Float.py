a = 1
b = 1.23456789101112131415
print(a)
print(b)
print(type(a))
print(type(b))

#import thư viện decimal
from decimal import*

getcontext().prec = 3


e=(Decimal(10)/Decimal(3))
print(e)

d=10/3
print(d)

from fractions import*
frac1 = Fraction(6,9)
frac2 = Fraction(3,8)
frac3 = frac1 + frac2

print(frac3)
print(type(frac3))

t = complex(2,5)
print(t)
print(t.real)
print(t.imag)

k = 11
h = 3
i = k//h #thương nguyên của k và h (kết quả luôn lớn hơb k/h)
u = k**h #lũy thừa của k với cơ số h
m = k%h #dư của thương k với h
print(i)
print(u)
print(m)
