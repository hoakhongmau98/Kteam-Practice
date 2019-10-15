def mod_7(numb):
	i = 0
	while i < numb:
		j = i
		i+=1
		if j%7 ==0:
			yield j
for i in mod_7(100):
	print(i)