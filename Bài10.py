#x = int(input('Nhập x: '))
#y = int(input('Nhập y: '))
x = 3
y = 5
lst_xy = []

''' Khởi tạo lst_xy bao giữ liệu chính
	vòng for đầu tiên sẽ tạo ra một list rỗng với thứ tự của x
	vòng lồng for thứ 2 sẽ lặp số lần y, truyền thẳng vào list rỗng 
	đã tạo phía trên, theo giá trị j*i
	kết thúc quay lại khởi tạo một list rỗng khác 
'''

for i in range(x):
	lst_xy.append([])
	for j in range(y):
		lst_xy[i].append(j*i)
print('Kết quả:\n',lst_xy)
