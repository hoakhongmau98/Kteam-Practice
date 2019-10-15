def so_luong(c,s):
	klq = 'error'
	for i in range(1,c+1):
		j = c-1
		if (2*i+4*j)==s:
			return i,j
		else:
			return klq
dap_an = so_luong(35,94)
print(dap_an)