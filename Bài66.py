def de_quy(n):
	if n ==0: 
		return 0
	elif n ==1:
		return 1
	else:
		return de_quy(n-1) + de_quy(n-2)
print(de_quy(7))
