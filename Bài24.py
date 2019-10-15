from math import sqrt
j = [('Up','5'),('Down','3'),('Left','3'),('Right','2')]
#Điểm gốc
p = [0,0]
x = 0
y = 0
'''while True:
	s = input('Nhập vào chuỗi hoạt động:')
	if nit s:
		break
	l.append(tuple(s.split(' ')))'''
#vòng lặp xử lý bước đi, nhận giá trị từ tuple truyền trả vào x,y
for i in range(len(j)):
	if j[i][0] == 'Down':
		y -= int(j[i][1])
	if j[i][0] == 'Up':
		y += int(j[i][1])
	if j[i][0] == 'Left':
		x -= int(j[i][1])
	if j[i][0] == 'Right':
		x += int(j[i][1])
#cách tính bằng: căn bậc 2 của tổng 2 bình phương của 2 tổng (x1,x2), (y1,y2)
print(int(sqrt(((p[0]+x)**2)+((p[1]+y)**2))))