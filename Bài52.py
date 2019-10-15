class Circle:
	def __init__(self,r_circle):
		self.R = r_circle
	def S_Circle(self):
		print(self.R**2*3.14)
Circle_a = Circle(5)
Circle_a.S_Circle()