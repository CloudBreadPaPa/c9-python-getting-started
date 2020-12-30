# 반복문(Loops) - 이하 루프

## For 루프

[For 루프](https://docs.python.org/3/reference/compound_stmts.html#the-for-statement)는 array 또는 collection의 각 항목을 순서대로 가져 와서 정의한 변수에 할당합니다.

``` python
names = ['Christopher', 'Susan']
for name in names:
    print(name)
```

## While 루프

[While 루프](https://docs.python.org/3/reference/compound_stmts.html#the-while-statement)는 조건이 true인 작업을 만날때까지 계속 작업을 수행합니다.

``` python
names = ['Christopher', 'Susan']
index = 0
while index < len(names):
    name = names[index]
    print(name)
    index = index + 1
```
