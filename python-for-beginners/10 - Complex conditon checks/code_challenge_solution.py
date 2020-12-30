# 하키 팀에 가입하면 유니폼 뒷면에 이름이 표시됩니다, 
# 그렇지만 유니폼은 이름의 모든 글자를 담을만큼 충분히 크지 않을 수도 있습니다.

# 사용자에게 이름을 묻습니다.
first_name = input('Please enter your first name: ')
# 사용자에게 성을 입력 받습니다.
last_name = input('Please enter your last name: ')

# 이름이 < 10 이고 성이 < 10 인 경우
#   유니폼에 성과 이름을 인쇄
# 이름이 >= 10 이고 성이 < 10 인 경우
#   이름의 첫 이니셜과 성 전체를 인쇄합니다.
# 이름이 < 10 이고 성이 >= 10 인 경우
#   전체 이름과 성의 첫 이니셜을 인쇄합니다.
# 이름이 >= 10 이고 성이 >= 10 인 경우
#   성만 인쇄합니다.

# 이름의 길이를 체크
if len(first_name) >=10:
    long_first_name = True
else:
    long_first_name = False

# 성의 길이를 체크
if len(last_name) >= 10:
    long_last_name = True
else:
    long_last_name = False
 
# 다양한 성과 이름 길이에 대해, 유니폼 인쇄 조합들을 평가
if long_first_name and long_last_name:
    print(last_name)
elif long_first_name:
    print(first_name[0:1] + '. ' + last_name)
elif long_last_name:
    print(first_name + ' ' + last_name[0:1] + '.')
else:
    print(first_name + ' ' + last_name)