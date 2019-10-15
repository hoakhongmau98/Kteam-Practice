str_a = [x for x in input('Nhập vào các phần tử (a,b,c,..): ').split(',')]
value = []
for i in str_a:
	int_a = int(i,2)
	if int_a%5:
		value.append(i)

print(','.join(value))
#if not intp%5:
#if not là cái quần què gì 