# 코드 실행 중에 발생하는 오류를 처리하는 함수를 생성하면, 
# 사용자에게 메시지가 표시되고 오류를 기록해 디버깅에 도움이 될 수 있습니다.

# 파라미터 :
#   error_code : 각각의 오류 유형에 할당 된, 고유한 오류 코드. 예시) "45"는 데이터형 변환 오류입니다.
#   error_severity :    0 - 치명적인(fatal) 오류가 발생하지 않아야합니다.
#                       1 - 심각한(severe) 오류 코드로 인해 계속 진행할 수 없습니다.
#                       2 - 경고(warning) 코드는 계속 진행 될 수 있지만, 정보가 누락 될 수 있습니다
#   log_to_db : 이 오류가 데이터베이스에 기록되어야 하는지를 여부를 설정합니다.
#   error_message : 사용자에게 표시하고 데이터베이스에 입력할, 오류 메시지
#   source_module : 오류를 생성 한 Python 모듈의 이름

def error_logger(error_code, error_severity, log_to_db, error_message, source_module):
    print('oh no error: ' + error_message)
    # 오류를 데이터베이스 또는 파일에 기록하는 코드가 있다고 가정합니다.

first_number = 10
second_number = 5

if first_number > second_number:
    # 이 함수 호출 패턴을 즉각적으로 이해하기 어렵습니다. 
    # 이해하려면 error_logger 함수의 정의를 찾아서 살펴 봐야합니다.
    error_logger(45,1,True,'Second number greater than first','adding_method')


if first_number > second_number:
    # 이 함수 호출은 전달하는 값이 함수의 파라미터에 매핑되는 방식으로 볼 수 있으므로, 
    # 이해하기 더 쉽습니다.
    error_logger(error_code=45, 
                 error_severity=1,
                 log_to_db=True,
                 error_message='Second number greater than first',
                 source_module='adding_method')
