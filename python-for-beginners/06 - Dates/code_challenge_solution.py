from datetime import datetime, timedelta

# 오늘의 날짜 출력
current_date = datetime.now()
print(current_date)

# 어제의 날짜 출력
one_day = timedelta(days=1)
yesterday = current_date - one_day
print('Yesterday was: ' + str(yesterday))

# 사용자에게 날짜 입력 요청
date_entered = input('Please enter a date (dd/mm/yyyy): ')
date_entered = datetime.strptime(date_entered, '%d/%m/%Y')

# 입력 받은 날짜로부터 1주 후 날짜 출력
one_week = timedelta(weeks=1)
one_week_later = date_entered + one_week
print('One week later it will be: ' + str(one_week_later))