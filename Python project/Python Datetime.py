# import datetime
# x = datetime.datetime.now()
# print(x)
# print(datetime.datetime(2022,10,3))

import datetime
x = datetime.datetime.now()
m = x.strftime("%b")
print(m)

n = x.strftime("%B")
print(n)

k = x.strftime("%m")
print(k)