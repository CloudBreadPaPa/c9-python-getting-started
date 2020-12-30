# 패키지(Packages)와 모듈(Modules)

## 모듈

[모듈](https://docs.python.org/3/tutorial/modules.html)을 사용하면 함수와 같은 재사용 가능한 코드를 별도의 파일에 저장할 수 있습니다. 모듈은 `import` 구문을 사용하여 참조할 수 있습니다.

``` python
# 모듈을 네임스페이스(namespace)로 import
import helpers
helpers.display('Not a warning')

# 모든 항목들을 네임스페이스로 import
from helpers import *
display('Not a warning')

# 특정 항목만 네임스페이스로 import
from helpers import display
display('Not a warning')
```

## 패키지(Packages)

[배포 패키지(Distribution packages)](https://packaging.python.org/glossary/#term-distribution-package)는 클래스 및 함수와 같은 리소스를 포함하는 외부 저장소의 파일입니다. 생성하는 대부분의 모든 Python 응용 프로그램은 하나 이상의 패키지를 사용합니다. 패키지에서 import는 생성 한 모듈과 동일한 구문을 따릅니다. [Python 패키지 인덱스](https://pypi.org/)에는 [pip](https://pip.pypa.io/en/stable/)를 사용하여 설치할 수있는 전체 패키지 목록이 있습니다.

## Virtual environments

[Virtual environments](https://docs.python.org/3.7/tutorial/venv.html)을 사용하면 격리 된 폴더에 패키지를 설치할 수 있습니다. 이를 통해 버전을 더 잘 관리 할 수 있습니다.
