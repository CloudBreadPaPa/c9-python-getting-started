import datetime
# 메시지와 현재 시간을 출력하는 print_time이라는 함수를 생성합니다.
def print_time():
    print('task completed')
    print(datetime.datetime.now())
    print() 

first_name = 'Susan'
# print_time() 함수를 호출해 메세지와 현재 시간을 표시합니다.
print_time()

for x in range(0,10):
    print(x)
# print_time() 함수를 호출해 메세지와 현재 시간을 표시합니다.
print_time()