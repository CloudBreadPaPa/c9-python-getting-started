# 현재 날짜와 시간을 얻으려면 datetime 라이브러리를 사용해야합니다.
from datetime import datetime

# now 함수는 현재 날짜와 시간을 리턴합니다.
today = datetime.now()

# 일, 월, 년, 시, 분, 초 function 사용해 날짜의 일부만 표시할 수 있습니다.
# 이 모든 함수는 정수(integer) 값을 반환합니다.
# 다른 문자열에 연결(concat)하기 전에 문자열로 변환해야 합니다.
print('Day: ' + str(today.day))
print('Month: ' + str(today.month))
print('Year: ' + str(today.year))

print('Hour: ' + str(today.hour))
print('Minute: ' + str(today.minute))
print('Second: ' + str(today.second))
