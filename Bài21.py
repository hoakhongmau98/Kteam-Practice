a = input("Nhập vào mật khẩu của bạn: ")
#a = '&$*^^$644bH'
#Duyệt qua từng trường hopwj và trả ra giá trị sau khi đã xét hết các giá trị.
def test_passwords(passwords):
	erron = []
	str_upper = 0
	str_lower = 0
	chr_note = ['!','@','#','$','%','^','&','*','(',')','-','_','=','+','`','~','.',',','<','>','/','?']
	numb_chr = 0
	str_number = 0
	for i in passwords:
		if i.isupper():
			str_upper +=1
		if i.islower():
			str_lower +=1
		if i in chr_note:
			numb_chr +=1
		if i.isdigit():
			str_number +=1
	if len(passwords) < 6:
		#Nếu điều kiện không khớp, return ngay vì không đạt điều kiện tạo mật khẩu
		return print('Mật khẩu của bạn quá ngắn')
	if len(passwords) > 12:
		#Nếu điều kiện không khớp, return ngay vì không đạt điều kiện tạo mật khẩu
		return print('Mật khẩu của bạn quá dài')
	if str_lower == 0:
		erron.append('Mật khẩu phải có chữ thường')
	if str_upper == 0:		
		erron.append('Mật khẩu phải có chữ hoa')
	if str_number ==0:
		erron.append('Mật khẩu phải có một ký tự là chữ số')
	if numb_chr == 0:
		erron.append('Mật khẩu phải chứa ký tự đặc biệt trong khoảng: [~,`,!,@,#,$,%,^,&,*,(,),_,+,-,=,<,>,?,.,/]')
	if len(erron) == 0 :
		print('*******************************************************************************************')
		print('Mật khẩu của bạn rất mạnh')
		print('*******************************************************************************************')
	elif len(erron) >0 and len(erron) <=1:
		print('Mật khẩu của bạn mạnh')
		print('*******************************************************************************************')
		print('-----Mật khẩu còn thiếu:-----')
		print('\n'.join(erron))
		print('*******************************************************************************************')
	elif len(erron) > 1:
		print('*******************************************************************************************')
		print('Mật khẩu của bạn quá yếu. vui lòng nhập lại mật khẩu')
		print('-----Mật khẩu còn thiếu:-----')
		print('\n'.join(erron))
		print('*******************************************************************************************')
	#print(len(erron))
	#print(str_lower)
	#print(str_upper)
	#print(numb_chr)
test_passwords(a)

