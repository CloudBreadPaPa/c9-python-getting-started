# 하키 팀에 가입하면 유니폼 뒷면에 이름이 표시됩니다, 
# 그렇지만 유니폼은 이름의 모든 글자를 담을만큼 충분히 크지 않을 수도 있습니다.
# 사용자에게 이름을 묻습니다.
# 사용자에게 성을 입력 받습니다.

# 이름이 < 10 이고 성이 < 10 인 경우
#   유니폼에 성과 이름을 인쇄
# 이름이 >= 10 이고 성이 < 10 인 경우
#   이름의 첫 이니셜과 성 전체를 인쇄합니다.
# 이름이 < 10 이고 성이 >= 10 인 경우
#   전체 이름과 성의 첫 이니셜을 인쇄합니다.
# 이름이 >= 10 이고 성이 >= 10 인 경우
#   성만 인쇄합니다.

# 다음 이름을 테스트합니다.
# 이름 : Susan  성 : Ibach
# 결과 : Susan Ibach
# 이름 : Susan  성 : ReallyLongLastName
# 결과 : Susan R.
# 이름 : ReallyLongFirstName  성 : Ibach
# 결과 : R. Ibach
# 이름 : ReallyLongFirstName  성 : ReallyLongLastName
# 결과 : ReallyLongLastName