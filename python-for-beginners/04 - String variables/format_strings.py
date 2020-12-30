# 사용자에게 이름과 성을 입력 받습니다.
first_name = input('What is your first name? ')
last_name = input('What is your last name? ')

# capitalize 함수는 다음과 같은 문자열을 리턴합니다.
# 첫 글자는 대문자이고 나머지 단어는 소문자
print ('Hello ' + first_name.capitalize() + ' ' \
       + last_name.capitalize())
