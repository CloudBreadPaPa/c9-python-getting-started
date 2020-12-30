x = 42
y = 0
try:
    print(x / y)
except ZeroDivisionError as e:
    # 선택 항목으로, "e" 값을 어딘가에 로깅합니다.
    print('Sorry, something went wrong')
except:
    print('Something really went wrong')
finally:
    print('This always runs on success or failure')
