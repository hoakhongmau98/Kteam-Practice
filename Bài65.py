def de_quy(n):
	if n==0:
		return 1
	else:
		return de_quy(n-1)+100
de_quy(5)
print(de_quy(5))