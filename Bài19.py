#lst_chr = [x for x in input('Nhập vào giá trị: ').split(',')]
lst_chr = [5,1,2,3,4,6,4,6,5,1,2,3,4,5]
lst_ood = []
for i in lst_chr:
	if i%2:
		lst_ood.append(i)
print(lst_ood)