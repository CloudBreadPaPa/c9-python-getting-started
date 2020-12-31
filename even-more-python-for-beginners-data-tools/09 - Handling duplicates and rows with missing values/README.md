# 중복 데이터와 missing value(누락된 값) 처리

머신러닝 트레이닝 데이터를 준비 할 때, 중복 row 제거와 missing value가 있는 row를 삭제 해야 하는 경우가 있습니다.

## 일반적인 기능

- [dropna](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.duplicated.html) missing value가 있는 row들을 삭제

- [duplicated](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.duplicated.html) 
이전 row와 비교해 중복 row인지 비교 후 True 또는 False로 표시

- [drop_duplicates](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop_duplicates.html) 중복 row들이 삭제된 DataFrame을 리턴

## Microsoft Learn 리소스

[Microsoft Learn](https://learn.microsoft.com/?WT.mc_id=python-c9-niner) 에서 관련 자습서를 살펴보세요.

- [Python과 Azure Notebooks을 이용한 머신러닝 소개](https://docs.microsoft.com/learn/paths/intro-to-ml-with-python/?WT.mc_id=python-c9-niner)

