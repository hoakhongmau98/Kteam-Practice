a = (1,2,3,4,5,6,7,8,9,10) 
lst = []
for i in a:
	if not i%2:
		lst.append(i)
print(tuple(lst))