country = 'CANADA'
# 입력 한 문자열을 소문자로 변환하고, 모두 소문자인 문자열과 비교하여 대소 문자를 구별하지 않고 비교합니다.
# 누군가가 CANADA 또는 Canada라고 입력해도, 모두 소문자로 변환해 비교했기 때문에 조건은 일치합니다.

if country.lower() == 'canada':
	print('Hello eh')
else:
	print('Hello')
