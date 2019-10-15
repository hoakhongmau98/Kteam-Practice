#Khi muốn in chuỗi ra dưới dạng text liền mạch, đầu tiên cần chuyển chuỗi đó sang dạng str
lst = []
for i in range(1000,3001):
	if not i%2:
		s = str(i)
		lst.append(s)
print(lst)
print(','.join(lst))