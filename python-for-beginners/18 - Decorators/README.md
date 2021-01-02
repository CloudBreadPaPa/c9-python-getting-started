# Decorators

[데코레이터(Decorators)](https://www.python.org/dev/peps/pep-0318/)는 Python의 코드 블록에 의미 나 기능을 추가한다는 점에서 속성(attribute)과 유사합니다. [Flask](http://flask.pocoo.org/) 또는 [Django](https://www.djangoproject.com/)와 같은 프레임 워크에서 자주 사용됩니다. Python 개발자로서 대부분의 경우, Decorator를 만들기 보다는 주로 사용하게 될 것입니다.

``` python
# Decorators 예시
@log(True)
def sample_function():
    print('this is a sample function')
```
