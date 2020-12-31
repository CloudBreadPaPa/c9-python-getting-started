class Presenter():
	def __init__(self, name):
		# 생성자(Constructor)
		self.name = name
	def say_hello(self):
		# 메서드(method)
		print('Hello, ' + self.name)

presenter = Presenter('Chris')
presenter.name = 'Christopher'
presenter.say_hello()