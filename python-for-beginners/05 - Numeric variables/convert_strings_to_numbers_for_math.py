first_num = input('Enter first number ')
second_num = input('Enter second number ')
# 숫자가 포함된 문자열 변수가 있는 경우
# 문자열을 숫자로 처리하고 싶다면, numeric datatype 으로 convert 해야 합니다
# int()는 문자열을 정수로 변환합니다. 예를 들어, 5, 8, 416, 506

print(int(first_num) + int(second_num))

# float()는 문자열을 decimal 또는 float로 변환합니다. 예를 들어, 3.14159, 89.5, 1.0
print(float(first_num) + float(second_num))
