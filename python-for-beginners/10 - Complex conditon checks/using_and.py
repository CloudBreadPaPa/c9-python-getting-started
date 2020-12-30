# 평균이 등급이 0.85 이상이고, 최하위 등급이 0.7이 아니면 이 학생은 우등생으로 분류합니다.
gpa = float(input('What was your Grade Point Average? '))
lowest_grade = input('What was your lowest grade? ')
lowest_grade = float(lowest_grade)

if gpa >= .85 and lowest_grade >= .70:
		print('You made the honour roll')
