import json

# Dictionary 객체 생성
person_dict = {'first': 'Christopher', 'last':'Harrison'}
# 필요에 따라 dictionary에 key/value pair를 추가
person_dict['City']='Seattle'

# staff dictionary 생성
staff_dict ={}
# person_dict를 "Program Manager"로 값 설정
staff_dict['Program Manager']=person_dict
# Dictionary를 JSON 객체로 변환
staff_json = json.dumps(staff_dict)

# JSON 객체 출력
print(staff_json)