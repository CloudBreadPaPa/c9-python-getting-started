# Calling APIs

다른 웹서버나 웹서비스에서 호스팅되는 어플리케이션을 Python으로 호출 할 수 있습니다. [Microsoft Azure Cognitive Services](https://docs.microsoft.com/azure/cognitive-services/?WT.mc_id=python-c9-niner)는 당신의 앱과 웹사이트에 AI 기능을 추가하기 위해, 코드로 호출 할 수 있는 여러 API가 제공됩니다.

코드 예제를 통해, AI 기능을 제공하는 [Computer Vision](https://docs.microsoft.com/azure/cognitive-services/computer-vision/?WT.mc_id=python-c9-niner?WT.mc_id=python-c9-niner)의 [Analyze Image](https://westus.dev.cognitive.microsoft.com/docs/services/5adf991815e1060e6355ad44/operations/56f91f2e778daf14a499e1fa0) 함수를 호출할 것입니다.

API를 호출하기 위한 준비사항 : 
- [API 키](https://azure.microsoft.com/try/cognitive-services/?WT.mc_id=python-c9-niner)가 있어야 API 호출이 가능
- 서비스의 address 또는 endpoint
- [API 문서](https://westus.dev.cognitive.microsoft.com/docs/services/5adf991815e1060e6355ad44/operations/56f91f2e778daf14a499e1fa?WT.mc_id=python-c9-niner?WT.mc_id=python-c9-niner)에서 제공하는 호출 할 메서드의 함수 이름
- [API 문서](https://westus.dev.cognitive.microsoft.com/docs/services/5adf991815e1060e6355ad44/operations/56f91f2e778daf14a499e1fa?WT.mc_id=python-c9-niner)에서 제공하는 함수의 파라미터 정보
- [API 문서](https://westus.dev.cognitive.microsoft.com/docs/services/5adf991815e1060e6355ad44/operations/56f91f2e778daf14a499e1fa?WT.mc_id=python-c9-niner)에서 제공하는 나열된 HTTP 헤더 정보
