# This code will show you how to call the Computer Vision API from Python
# You can find documentation on the Computer Vision Analyze Image method here
# https://westus.dev.cognitive.microsoft.com/docs/services/5adf991815e1060e6355ad44/operations/56f91f2e778daf14a499e1fa

# 이 코드는 Python에서 Computer Vision API를 호출하는 방법을 보여줍니다.
# Computer Vision의 Analyze Image 메서드 대한 문서는 여기에서 찾을 수 있습니다.
# https://westus.dev.cognitive.microsoft.com/docs/services/5adf991815e1060e6355ad44/operations/56f91f2e778daf14a499e1fa

# Use the requests library to simplify making a REST API call from Python 
# requests 라이브러리를 사용하여 Python에서 간단하게 REST API 호출을 진행합니다.
import requests

# We will need the json library to read the data passed back 
# by the web service
# 웹 서비스의 응답(Response)를 처리하려면 json 라이브러리가 필요합니다.
import json

# 아래 Vision_service_address를 자신에게 맞는 Computer Vision API 서비스의 주소로 수정해야 합니다.
vision_service_address = "https://koreacentral.api.cognitive.microsoft.com/vision/v2.0/"  # 한국지역

# 호출하려는 API 함수의 이름을 주소에 추가합니다.
address = vision_service_address + "analyze"

# analyze image 함수의 문서에 따르면 세 가지의 Optional(선택적) 파라미터가 있습니다 : language, details, visualFeatures 파라미터
parameters  = {'visualFeatures':'Description,Color',
               'language':'en'}

# SUBSCRIPTION_KEY를 자신의 Computer Vision 서비스의 키로 수정하세요.
subscription_key = "xxxxxxxxxxxxxxxxxxxxxxxxxxx"

# 분석할 이미지가 포함된 파일을 열어서 파일 오브젝트로 가져옵니다.
image_path = "./TestImages/PolarBear.jpg"
image_data = open(image_path, 'rb').read()

# analyze image 함수 문서에서 기술한대로, HTTP 헤더에 구독 키와 content-type을 지정합니다.
# content-type 값은 "application/octet-stream" 입니다.
headers    = {'Content-Type': 'application/octet-stream',
              'Ocp-Apim-Subscription-Key': subscription_key}

# analyze image 함수 문서에서 가이드 하는 것처럼, HTTP POST 방식으로 함수를 호출합니다.
response = requests.post(address, headers=headers, params=parameters, data=image_data)

# HTTP 호출에서 오류가 생기면, 예외를 발생 시킵니다.
response.raise_for_status()

# 리턴 받은 JSON 결과를 출력합니다.
results = response.json()
print(json.dumps(results))

print('requestId')
print (results['requestId'])

print('dominantColorBackground')
print(results['color']['dominantColorBackground'])

print('first_tag')
print(results['description']['tags'][0])

for item in results['description']['tags']:
    print(item)

print('caption text')
print(results['description']['captions'][0]['text'])

