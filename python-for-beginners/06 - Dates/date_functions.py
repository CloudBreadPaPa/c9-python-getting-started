# 현재 날짜와 시간을 얻으려면 datetime 라이브러리를 사용해야합니다.
from datetime import datetime, timedelta
# now 함수는 현재 날짜와 시간을 리턴합니다.
today = datetime.now()

print('Today is: ' + str(today))
# timedelta를 사용하여 날짜에 일 또는 주를 더하거나 뺄 수 있습니다.
one_day = timedelta(days=1)
yesterday = today - one_day
print('Yesterday was: ' + str(yesterday))

one_week = timedelta(weeks=1)
last_week = today - one_week
print('Last week was: ' + str(last_week))

