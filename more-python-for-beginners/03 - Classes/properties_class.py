class Presenter():
	def __init__(self, name):
		# 생성자(Constructor)
		self.name = name

	@property
	def name(self):
		print('Retrieving name...')
		return self.__name
	@name.setter
	def name(self, value):
		# 이곳에 검증 코드가 있다고 가정
		print('Validating name...')
		self.__name = value

presenter = Presenter('Chris')
presenter.name = 'Christopher'
print(presenter.name)