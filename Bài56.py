try:
	print(5/0)
except ZeroDivisionError:
	print('không thể chia cho 0')
finally:
	print('hoàn thành phép chia')