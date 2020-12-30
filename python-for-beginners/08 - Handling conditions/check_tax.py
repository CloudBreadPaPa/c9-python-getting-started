# 세금 계산
# $1.00 이상의 구매는 모두 7%의 세금이 부과됩니다.

price = input('how much did you pay? ')

# 문자열을 숫자형으로 변환
price = float(price)

# price가 1.00 이상인지 체크
if price >= 1.00:
	# $1.00 이상의 구매는 모두 7%의 세금이 부과됩니다.
	tax = .07
	print('Tax rate is: ' + str(tax))
