price = input('how much did you pay? ')
price = float(price)

if price >= 1.00:
	# $1.00 이상의 비용은 모두 7%의 세금이 부과됩니다.
	# 들여 쓰기(indent)된 모든 구문은 price >= 1.00 인 경우에만 실행됩니다.
	tax = .07
	print('Tax rate is: ' + str(tax))
else:
	# 그 외에는 세금을 부과하지 않습니다.
	# 들여 쓰기된 모든 구문은 가격이 $1 미만인 경우에 실행됩니다.
	tax = 0
	print('Tax rate is: ' + str(tax))
