# calculator 함수를 생성
# 이 함수는 세개의 파리미터를 입력받습니다.
# first_number : 수치 연산을 위한 숫자 값
# second_number : 수치 연산을 위한 숫자 값
# operator : 'add' 또는 'minus'라는 단어
# 함수의 operator 파리미터로 전달된 값에 따라, 더하거나 뺀 두 숫자의 결과를 출력해야 합니다.

def calculator(first_number, second_number, operation):
    if operation.upper() == 'ADD':
        return(float(first_number) + float(second_number))
    elif operation.upper() =='SUBTRACT':
        return(float(first_number) - float(second_number))
    else:
        return('Invalid operation please specify ADD or SUBTRACT')

# 6, 4, add 값으로 함수를 테스트하고, 결과로 10을 출력해야 합니다.
print('Adding 6 + 4 = ' + str(calculator(6,4,'add')))

# 6, 4, subtract 값으로 함수를 테스트하고, 결과로 2를 출력해야 합니다.
print('Subtracting 6 - 4 = ' + str(calculator(6,4,'subtract')))

# 6, 4, divide 값으로 함수를 테스트하고, 실행 결과는 에러 메세지를 출력해야 합니다.
print('Dividing 6 / 4 = ' + str(calculator(6,4,'divide')))