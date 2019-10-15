dic_n = {}
def directory(n):
	for i in range(1,n+1):
		values = i*i
		dic_n[i] = values
	print(dic_n)
print(directory(9))
