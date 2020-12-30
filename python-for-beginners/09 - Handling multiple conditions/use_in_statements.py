province = input("What province do you live in? ")
tax = 0
# 여러 값의 비교가 동일한 결과을 출력하는 경우, in 연산자로 비교항목을 조합(combine)하여 리스트 후 체크 가능합니다.

if province in('Alberta','Nunavut','Yukon'):
	tax = 0.05
elif province == 'Ontario':
	tax = 0.13
else:
	tax = 0.15
print(tax)