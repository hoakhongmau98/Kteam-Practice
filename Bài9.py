import math
from math import *
value = []
def Math_Q(D):
	C = 50
	H = 30
	return round(sqrt(((2*C*D)/H)))
str_D = input('Nhập chuỗi cần xử lý: ')
lst_D = str_D.split(',')
#lst_D = [100,150,180]
for i in range(len(lst_D)):
	value.append(Math_Q(int(lst_D[i])))

print('Chuỗi sau khi thực hiện phương trình:',value)
