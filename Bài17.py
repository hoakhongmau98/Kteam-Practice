a = 'Quản Trị Mạng'
str_a = 0
str_A = 0
for i in a:
	if i.isupper():
		str_A =str_A+1
	if i.islower():
		str_a = str_a+1
print(str_A)
print(str_a)