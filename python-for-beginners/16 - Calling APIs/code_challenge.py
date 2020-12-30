# 도전과제 # 1
# Azure Custom Vision 서비스를 생성하세요.
# 이미지를 분석하고 설명하는 JSON 응답(Response)을 리턴 받습니다.
# call_api.py는 거의 완성 된 코드이지만, 다음 과정을 추가로 진행해야만 합니다.
#   Azure에서 Custom Vision Service 만들기
#   API Key 업데이트
#   서비스 주소 업데이트
#   이미지 파일과 위치 확인 후 웹서비스로 전달


# 보너스 도전과제
# 계속 Python 코딩 능력이 향상되고 있습니다. 스스로 조금만 더 노력해 보세요.
# 이미, 컴퓨터 비전 서비스의 한 기능을 호출했습니다. 이제 다른 함수를 호출해 보세요.
# analyze 함수 대신 OCR 함수를 호출해 보시길 추천드립니다.
# 참고문서
# https://docs.microsoft.com/azure/cognitive-services/Computer-vision/concept-recognizing-text#ocr-optical-character-recognition-api
# https://westus.dev.cognitive.microsoft.com/docs/services/5adf991815e1060e6355ad44/operations/56f91f2e778daf14a499e1fc
# 위의 문서를 참조하여,
#   - 정확한 호출 주소와 함수명
#   - 함수에 전달할 파라미터
#   - 함께 전송해야 하는 HTTP 헤더
# 텍스트가 포함 된 이미지 파일을 OCR 서비스로 업로드하고, 리턴된 JSON에서 OCR로 리턴된 텍스트 문자열을 확인 하세요.
