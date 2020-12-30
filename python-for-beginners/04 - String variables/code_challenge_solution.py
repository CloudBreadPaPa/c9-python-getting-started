# 사용자에게 이름을 입력받고 변수에 저장
first_name = input('What is your first name? ')
# 사용자에게 성을 입력받고 변수에 저장
last_name = input('What is your last name? ')

# 전체 이름을 모두 출력
# 성과 이름 사이에 공백이 있는지 확인하세요.
# 이름과 성의 첫 글자가 대문자인지 확인하세요
# 나머지 이름은 소문자인지 확인하세요.
print(first_name.capitalize() + ' ' + last_name.capitalize())