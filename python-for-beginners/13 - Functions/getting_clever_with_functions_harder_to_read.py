# name을 파라미터로 입력 받아 첫 글자를 대문자로 반환하는 get_initial 함수를 생성합니다.
# 파라미터:
#   name: 사람의 이름
# 리턴값:
#   파라미터로 전달된 이름의 첫 글자를 대문자로 변환한 값
def get_initial(name):
    initial = name[0:1].upper()
    return initial

# 이름을 요청하고 이니셜을 리턴
first_name = input('Enter your first name: ')
middle_name = input('Enter your middle name: ')
last_name = input('Enter your last name: ')

# get_initial 함수를 호출해 각 이름의 첫 글자를 리턴 받음
print('Your initials are: ' \
    + get_initial(first_name) \
    + get_initial(middle_name) \
    + get_initial(last_name))