# name을 파라미터로 받고 이름의 첫 글자를 대문자로 리턴하는 get_initial 함수를 생성합니다.
# 매개 변수 :
#   name : 사람의 이름
# 리턴 값 :
#   파라미터로 전달된 이름의 첫 글자를 대문자로 리턴

def get_initial(name):
    initial = name[0:1].upper()
    return initial


# 이름을 입력받고 이니셜을 리턴합니다.
first_name = input('Enter your first name: ')
# 이름의 이니셜을 가져오기 위해 get_initial 함수를 호출
first_name_initial = get_initial(first_name)

middle_name = input('Enter your middle name: ')
# 이름의 이니셜을 가져오기 위해 get_initial 함수를 호출
middle_name_initial = get_initial(middle_name)

last_name = input('Enter your last name: ')
# 이름의 이니셜을 가져오기 위해 get_initial 함수를 호출
last_name_initial = get_initial(last_name)

print('Your initials are: ' + first_name_initial \
    + middle_name_initial + last_name_initial)