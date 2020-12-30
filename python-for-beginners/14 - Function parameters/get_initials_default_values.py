# name을 파라미터로 받고 이름의 첫 글자를 대문자로 리턴하는 함수를 생성합니다.
# 매개 변수 :
#   name : 사람의 이름
#   force_uppercase : 이니셜을 대문자로 표시할지 여부를 설정하고, 기본값은 True입니다.
# 리턴 값 :
#   파라미터로 전달된 이름의 첫 글자를 대문자로 리턴

def get_initial(name, force_uppercase=True):
    if force_uppercase:
        initial = name[0:1].upper()
    else:
        initial = name[0:1]
    return initial

# 이름을 입력받고 이니셜을 리턴합니다.
first_name = input('Enter your first name: ')

# get_initial 함수를 호출하지만, force_uppercase 값을 전달하지 않아 기본값이 사용됩니다.
first_name_initial = get_initial(first_name) 

print('Your initial is: ' + first_name_initial)