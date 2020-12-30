# Error handling

Python의 에러 처리(error handling)는 [try/except/finally](https://docs.python.org/3.7/reference/compound_stmts.html#except)를 사용하여 처리됩니다.


Python에는 수많은 [내장된 예외(built-in exceptions)](https://docs.python.org/3.7/library/exceptions.html)가 있습니다. `except` 블록을 생성 할 때는 [계층 구조](https://docs.python.org/3.7/library/exceptions.html#exception-hierarchy)에 따라 가장 하위의 구체적인 예외 처리부터 가장 일반적인 예외 처리까지 생성해야합니다.
