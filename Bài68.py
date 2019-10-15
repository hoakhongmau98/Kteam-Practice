def fnc_a(c):
	for i in range(0,c+1):
		if not i%2:
			yield i
n = 10
lst_a = []
for i in fnc_a(n):
	lst_a.append(str(i))

print(','.join(lst_a))