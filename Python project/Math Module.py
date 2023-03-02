import math
# x=10.5
# print(math.ceil(x))
#
# x=-10
# print(math.fabs(x))
#
# x=5
# print(math.factorial(x))
#
# x=0.5
# print(math.floor(x))
#
# l=[10,20,30,40]
# print(math.fsum(l))
#
# print(math.sqrt(16))
x=1
print(math.nextafter(x, math.inf))
print(math.nextafter(x, -math.inf))
print(math.nextafter(x, 0.0))
print(math.nextafter(x, math.copysign(math.inf, x)) )