# 이름의 이니셜을 리턴하는 함수를 생성합니다.
# 매개 변수 :
#   name : 사람의 이름
#   force_uppercase : 이니셜을 항상 대문자로 표시할지 여부를 설정합니다.
# 리턴 값 :
#   파라미터로 전달된 이름의 첫 글자를 대문자로 리턴

def get_initial(name, force_uppercase):
    if force_uppercase:
        initial = name[0:1].upper()
    else:
        initial = name[0:1]
    return initial

 # 이름을 입력받아 이니셜을 리턴합니다.
first_name = input('Enter your first name: ')

# get_initial을 호출해 이름의 첫 이니셜을 가져옵니다.
# 명시적으로 파라미터를 전달해 사용하면 순서에 관계없이 매개 변수를 지정할 수 있습니다.
first_name_initial = get_initial(force_uppercase=True, \
                                name=first_name) 

print('Your initial is: ' + first_name_initial)