lst_chr = []
for i in range(2):
	lst_chr.append(input('Chuỗi:'))
for i in range(2):
	if len(lst_chr[1]) > len(lst_chr[0]):
		print(lst_chr[1])
	elif len(lst_chr[1]) == len(lst_chr[0]):
		print(lst_chr[0])
		print(lst_chr[1])
	else:
		print(lst_chr[0])