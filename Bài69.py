def fnc_a(c):
	for i in range(c+1):
		if i%5 ==0 and i%7 ==0:
			yield i

n = 100
#lst_a = []
#for i in fnc_a(n):
	#lst_a.append(str(i))
lst_a = [str(x) for x in fnc_a(n)]
print(lst_a)