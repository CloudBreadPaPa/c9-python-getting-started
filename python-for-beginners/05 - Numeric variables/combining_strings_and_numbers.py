days_in_feb = 28

# print 함수는 숫자나 문자열을 출력할 수 있습니다
print(days_in_feb)

# + 연산자는 두 개의 숫자를 더하거나 두 문자열을 연결할 수 있습니다
# 하지만, 숫자와 문자열을 + 하도록 전달하면 오류를 발생시킵니다.
print(days_in_feb + ' days in February')

# 결과를 출력하려면 숫자를 문자열로 변환(convert)해야합니다. 
# 이 코드는 잘 작동합니다
print(str(days_in_feb) + ' days in February')
