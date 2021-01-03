class Person:
	def __init__(self, name):
		self.name = name
	def say_hello(self):
		print('Hello, ' + self.name)

class Student(Person):
	def __init__(self, name, school):
		super().__init__(name)
		self.school = school
	def sing_school_song(self):
		print('Ode to ' + self.school)
	def __str__(self):  # 오버라이딩
		return self.name

student = Student('Christopher', 'UVM')
student.say_hello()
student.sing_school_song()

# 누구신가요?
print(isinstance(student, Student))
print(isinstance(student, Person))
print(issubclass(Student, Person))

print(student)  # 오버라이딩 출력
