# 현재 날짜와 시간을 얻으려면 datetime 라이브러리를 사용해야합니다.
from datetime import datetime

current_date = datetime.now()
# now 함수는 현재 날짜와 시간을 datetime 객체로 반환합니다.

# datetime 객체를 다른 문자열에 연결하기 전에 문자열로 변환해야합니다.
print('Today is: ' + str(current_date))
