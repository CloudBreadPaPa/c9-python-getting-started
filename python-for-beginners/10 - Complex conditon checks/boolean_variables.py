# 요구사항이 장학생 요건에 적절한지 체크합니다. 
gpa = float(input('What was your Grade Point Average? '))
lowest_grade = float(input('What was your lowest grade? '))


# Boolean 변수에 True/False 값을 저장 가능합니다.
if gpa >= .85 and lowest_grade >= .70:
	honour_roll = True
else:
	honour_roll = False


# 학생이 장학생인지 확인해야하는 경우 앞에서 세팅 한 Boolean 변수만 확인하면 됩니다.
if honour_roll:
	print('You made honour roll')
