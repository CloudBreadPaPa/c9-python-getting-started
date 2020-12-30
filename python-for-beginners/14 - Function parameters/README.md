# 함수 파라미터(Function parameters)

함수를 사용하면 반복되는 코드를 가져와 필요할 때, 호출 할 수 있는 모듈로 재사용할 수 있습니다. 함수는 `def` 키워드로 정의되며, 코드에서 함수가 호출되기 전에 선언되어야합니다. 함수는 파라미터(parameter-매개 변수)를 사용할 수 있고, 값을 리턴 할 수 있습니다.

- [Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)

```python
def function_name(parameter):
    # 실행할 코드
    return value
```

매개 변수에 [기본값(default value)](https://docs.python.org/3/tutorial/controlflow.html#default-argument-values)을 할당하여 함수가 호출 될 때 선택 사항으로 지정할 수 있습니다.

```python
def function_name(parameter=default):
    # 실행할 코드
    return value
```

함수를 호출 할 때 위치를 지정해 표기(Positional notation)하거나 [명명된 표기법(named notation)](https://docs.python.org/3/tutorial/controlflow.html#keyword-arguments)을 사용하여 파라미터 값을 지정할 수 있습니다.

```python
def function_name(parameter1, parameter2):
    # 실행할 코드
    return value

# 위치 지정 표기법(Positional notation)은 파라미터가 선언 된 것과 같은 순서로 인자값을 전달합니다.
result = function_name(value1,value2)

# 명명된 표기법(Named notation)
result = function_name(parameter1=value1, parameter2=value2)
```
