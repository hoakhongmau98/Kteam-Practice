my_lst = []
my_tuple = ()

def convert(n):
	my_lst = n.split(',')
	my_tuple = tuple(my_lst)
	print(my_lst)
	print(my_tuple)	
chr_cvt = ('85,2,4,6,444,62,48,41,565,48,52,46,44')

#chr_cvt = ()
#chr_cvt = input('nhập vào chuỗi xử lý')
#print(type(chr_cvt))
convert(chr_cvt)
