# 체크인시 이름을 기준으로 다른 방에 사람을 배정하세요.
# 완료되면, Anna는 AB 방에 있어야합니다.
# Bob은 AB 방에 있어야합니다.
# Charlie는 C 방에 있어야합니다.
# Khalid Haque는 OTHER 방에 있어야합니다.
# Xin Zhao는 Z 방에 있어야합니다.
# 사용자에게 이름을 묻습니다.

name = input('What is your name? ')

# 이름이 A 또는 B로 시작하는 경우
# AB 방으로 배정하세요.
first_letter = name[0:1]
if first_letter.upper() in ('A','B'):
    room = 'AB'
# 이름이 C로 시작하는 경우
# C 방으로 배정하세요.
elif first_letter.upper() == 'C':
    room = 'C'
else:
    # 이름이 다른 문자로 시작하면 성을 문의합니다.
    # 성이 Z로 시작하면 Z 방으로 가라고 말하세요
    last_name = input('what is your last name? ')
    last_name_first_letter = last_name[0:1]
    # 성이 다른 문자로 시작하면 OTHER 방으로 가라고 말하세요.
    if last_name_first_letter == 'Z':
        room = 'Z'
    else:
        room = 'OTHER'
print('Please go to room ' + room)

