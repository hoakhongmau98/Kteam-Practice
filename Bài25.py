'''nhập vào 1 mảng
sử dung set để lấy ra các keyword
vòng lặp từng keyword với mảng chính để tìm ra số lần trùng nhau'''
a = 'New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3'
lst_str = []
lst_str = a.split(' ')
lst_point = [0]
#print(lst_str)
set_str = sorted(list(set(lst_str)))

#print(set_str)
for i in range(len(set_str)):
	for x in lst_str:
		if set_str[i] == x:
			lst_point[i] = lst_point[i]+1
	lst_point.append(0)
for i in range(len(set_str)):
	print(set_str[i],':',lst_point[i])