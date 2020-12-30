# 사용자에게 번호 입력 받음
first_number = input('Enter a number: ')

# 사용자에게 두 번째 숫자를 입력 받음
second_number = input('Enter another number: ')

# 입력 받은 두 숫자의 합을 계산
answer = float(first_number) + float(second_number)

# 'first number + second number = answer' 출력
# 예를 들어 4와 6을 입력하면 출력은
# 4 + 6 = 10
print(first_number + ' + ' + second_number + ' = ' + str(answer))

# 소수점 이하 자릿수를 원하지 않을 경우, 결과를 반올림 할 수 있습니다.
print(first_number + ' + ' + second_number + ' = ' + str(round(answer)))
