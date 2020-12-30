# 이 코드의 오류를 수정하고 아래 구문을 테스트합니다.
# 2.00을 입력하면 "세율: 0.07"이라는 메시지가 출력됩니다.
# 1.00을 입력하면 "세율: 0.07"이라는 메시지가 출력됩니다.
# 0.50을 입력하면 "세율: 0"이라는 메시지가 출력됩니다.

price = input('how much did you pay? ')
price = float(price)

if price >= 1.00:
	tax = .07
	print('Tax rate is: ' + str(tax))
else:
    tax = 0
    print('Tax rate is: ' + str(tax))