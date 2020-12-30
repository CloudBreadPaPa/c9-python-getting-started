# datetime.now() 함수를 호출하기 위해, datetime 라이브러리에서 datetime 클래스를 import합니다.
from datetime import datetime

# print_time이라는 함수를 생성합니다. 이 함수는 메시지와 현재 시간을 출력합니다
def print_time():
    print('task completed')
    print(datetime.now())
    print()

first_name = 'Susan'
# print_time() 함수를 호출하여 메시지와 현재 시간을 표시합니다.
print_time()

for x in range(0,10):
    print(x)
# print_time() 함수를 호출하여 메시지와 현재 시간을 표시합니다.
print_time()