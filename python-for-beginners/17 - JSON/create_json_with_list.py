import json

# Dictionary 객체 생성
person_dict = {'first': 'Christopher', 'last':'Harrison'}
# 필요에 따라 dictionary에 key/value pair를 추가
person_dict['City']='Seattle'

# List 객체를 생성
languages_list = ['CSharp','Python','JavaScript']

# List 객체를 dictionary에 languages를 key로 추가 
person_dict['languages']= languages_list

# Dictionary를 JSON 객체로 변환
person_json = json.dumps(person_dict)

# JSON 객체 출력
print(person_json)