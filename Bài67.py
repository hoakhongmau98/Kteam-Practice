def de_quy(n):
	if n ==0: 
		return 0
	elif n==1:
		return 1
	else: 
		return de_quy(n-1) + de_quy(n-2)
n = 7
#lấy dữ liệu từ for truyền vào de_quy(x)
#dữ liệu ra sẽ được định dạng là str và truyền vào list value
value = [str(de_quy(x)) for x in range(0,n+1)]
print(de_quy(n))
print(','.join(value))