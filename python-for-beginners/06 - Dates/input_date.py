# datetime, timedelta 모듈을 import 합니다.
from datetime import datetime, timedelta

# 사용자에게 날짜를 입력 받을 때 날짜 형식을 알려주면 좋습니다.
birthday = input('When is your birthday (dd/mm/yyyy)? ')

# 날짜가 포함 된 문자열을 날짜 객체로 변환 할 때 변환할 날짜 형식을 지정해야합니다.
# 날짜가 지정된 형식이 아니면 Python은 예외를 발생시킵니다
birthday_date = datetime.strptime(birthday, '%d/%m/%Y')

print ('Birthday: ' + str(birthday_date))

# 문자열을 날짜 객체로 변환했기 때문에 timedelta와 같은 날짜 및 시간 함수를 사용할 수 있습니다.
one_day = timedelta(days=1)
birthday_eve = birthday_date - one_day
print('Day before birthday: ' + str(birthday_eve))
