# Handling conditions

조건부(Condition) 실행은 [if](https://docs.python.org/3/reference/compound_stmts.html#the-if-statement) 문을 사용하여 처리 할 수 있습니다. `elif`를 추가하면 여러 조건을 추가 가능합니다.

`if` 구문

```python
if expression:
    # 실행할 코드
elif expression:
    # 실행할 코드
else:
    # 실행할 코드
```

[Boolean 연산자](https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not)

- **x *or* y** - x 또는 y가 true이면 구문이 실행됩니다.


[비교(Comparison) 연산자](https://docs.python.org/3/library/stdtypes.html#comparisons)

- < 미만
- < 초과
- == 같음
- \>= 이상(같거나 큼)
- <= 이하(같거나 작음)
- != 같지 않음
- **x *in* [a,b,c]** x 값이 a, b, c 중의 한 값과 일치하는가?