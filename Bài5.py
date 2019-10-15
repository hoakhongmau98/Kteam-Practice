#class chuyển đổi
class Convert_String:
	def __init__(self,chr_cvt):
		self.string = chr_cvt
	def string_cvt(self):
		return self.string.upper()
#phương thức nhập vào từ bàn phím
chr_a = input('Nhập vào chuỗi cần chuyển đổi: ')
string_A = Convert_String(chr_a)
#Nhập vào trực tiếp
#string_A = Convert_String('huyền chi')
print(string_A.string_cvt())




