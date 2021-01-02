# 이 코드에서는 Python으로 손쉽게 Computer Vision API를 호출하는 방법을 소개해 드립니다.
# Comupter Vision 이미지 분석 API method에 대한 문서는 이곳에서 참고하세요.
# https://westus.dev.cognitive.microsoft.com/docs/services/5adf991815e1060e6355ad44/operations/56f91f2e778daf14a499e1fa

# SQLER의 https://www.sqler.com/board_CSharp/1095782 강좌 참조

# requests 라이브러리를 사용하여 Python에서 간단하게 REST API 호출을 진행합니다.
import requests

# 웹 서비스의 응답(Response)를 처리하려면 json 라이브러리가 필요합니다.
import json

# SUBSCRIPTION_KEY를 자신의 Computer Vision 서비스의 키로 수정하세요.
SUBSCRIPTION_KEY = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

# 아래 Vision_service_address를 자신에게 할당된 Computer Vision API 서비스의 주소로 수정해야 합니다. 
# 유료 가입 계정과 7일 체험 계정의 endpoint가 다를 수 있습니다. 맨 뒤의 "/v2.0/"을 확인하세요.
vision_service_address = "https://westcentralus.api.cognitive.microsoft.com/vision/v2.0/" 

# 호출하려는 API 함수의 이름을 주소에 추가합니다.
address = vision_service_address + "analyze"

# analyze image 함수의 문서에 따르면 세 가지의 Optional(선택적) 파라미터가 있습니다 : language, details, visualFeatures 파라미터
parameters  = {'visualFeatures':'Description,Color',
               'language':'en'}

# 분석할 이미지가 포함된 파일을 열어서 파일 오브젝트로 가져옵니다.
image_path = "./TestImages/PolarBear.jpg"
image_data = open(image_path, "rb").read()

# analyze image 함수 문서에서 기술한대로, HTTP 헤더에 구독 키와 content-type을 지정합니다.
# content-type 값은 "application/octet-stream" 입니다.
headers    = {'Content-Type': 'application/octet-stream',
              'Ocp-Apim-Subscription-Key': SUBSCRIPTION_KEY}

# analyze image 함수 문서에서 가이드 하는 것처럼, HTTP POST 방식으로 함수를 호출합니다.
response = requests.post(address, headers=headers, params=parameters, data=image_data)

# HTTP 호출에서 오류가 생기면, 예외를 발생 시킵니다.
response.raise_for_status()

# 리턴 받은 JSON 결과를 출력합니다.
results = response.json()
print(json.dumps(results))
