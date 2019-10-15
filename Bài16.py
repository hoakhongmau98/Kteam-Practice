a = 'hello world!! 123'
numb_a = 0
str_a = 0
for i in range(len(a)):
	#isdigit() - phương thức kiểm tra chuỗi có phải là số hay không
	if a[i].isdigit():
		str_a = str_a +1
	#isalpha() - Phương thức kiểm tra chuỗi có phải là ký tự hay không
	if a[i].isalpha():
		numb_a = numb_a +1
print(numb_a)
print(str_a)
#print(a[-1].isdigit())