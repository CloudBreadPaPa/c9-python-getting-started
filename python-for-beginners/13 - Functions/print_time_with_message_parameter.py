from datetime import datetime

# 현재 시간과 작업 이름을 인쇄하는 함수를 생성합니다.
# 다음 매개 변수 기능 :
#   task_name : 출력시 표시 할 작업의 이름
def print_time(task_name):
    print(task_name)
    print(datetime.now())
    print()

first_name = 'Susan'
# print_time() 함수를 호출해 메세지와 현재 시간을 표시합니다.
# 완료된 task_name을 파라미터로 전달합니다.
print_time('first name assigned')

for x in range(0,10):
	print(x)
# print_time() 함수를 호출해 메세지와 현재 시간을 표시합니다.
# 완료된 작업 이름을 전달합니다.
print_time('loop completed')
