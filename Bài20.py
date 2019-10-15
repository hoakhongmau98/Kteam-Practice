money = 0
while True:
	s = input('Nhập vào nhật ký giao dịch:')
	#s = 'D 200'
	if not s:
		break
	values = s.split(' ')
	operation = values[0]
	amount = int(values[1])
	if operation == 'D':
		money = money + amount
	if operation == 'W':
		money-=amount
	else:
		pass
print(money)