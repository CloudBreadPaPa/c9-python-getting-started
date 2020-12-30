# calculator 함수 생성
# 함수는 세개의 파라미터를 받습니다.
# first_number : 수치 연산을 위한 숫자 값
# second_number : 수치 연산을 위한 숫자 값
# operator : 'add' 또는 'subtract'라는 단어를 입력 받으며, 기본 값은 'add' 입니다.
# 함수는 operator로 전달된 파라미터에 따라 더하거나 뺀 두 숫자의 결과를 리턴해야합니다.

def calculator(first_number, second_number, operation='ADD'):
    if operation.upper() == 'ADD':
        return(float(first_number) + float(second_number))
    elif operation.upper() =='SUBTRACT':
        return(float(first_number) - float(second_number))
    else:
        return('Invalid operation please specify ADD or SUBTRACT')


# 6, 4 값으로 함수를 테스트하고, 결과로 10을 출력해야 합니다.
print('Adding 6 + 4 = ' + str(calculator(first_number=6, second_number=4)))

# 6, 4, subtract 값으로 함수를 테스트하고, 결과로 2을 출력해야 합니다.
print('Subtracting 6 - 4 = ' + str(calculator(first_number=6, second_number=4, operation='subtract')))
