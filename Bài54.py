class Shape:
	s_shape = 0
	def __init__(self,chieu_rong):
		self.r = chieu_rong
	def dien_tich(self):
		s_shape = self.r*self.r
		print(s_shape)
class Square(Shape):
	def __init__(self,chieu_rong,chieu_dai):
		super().__init__(chieu_rong)
		self.d = chieu_dai
	def dien_tich(self):
		s_shape = self.r * self.d 
		print(s_shape)

shape_a = Shape(5)
shape_a.dien_tich()
shape_b = Square(10,15)
shape_b.dien_tich()


	