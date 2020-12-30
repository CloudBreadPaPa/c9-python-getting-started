# 문자열 변수에 사용할 수있는 여러 문자열 함수가 있습니다.
sentence = 'The dog is named Sammy'

# upper 함수는 문자열을 대문자로 리턴합니다.
print(sentence.upper())

# lower 함수는 문자열을 소문자로 리턴합니다.
print(sentence.lower())

# capitalize 함수는 첫 글자를 대문자로, 나머지 문자열은 소문자로 된 문자열을 리턴합니다.
print(sentence.capitalize())

# count will count the number of occurrences of the value specified in the string, in this case how many times the letter 'a' appears
# count는 문자열에 지정된 value의 발생 빈도를 리턴합니다. 이 경우 문자 'a'가 나타나는 횟수가 리턴됩니다.
print(sentence.count('a'))
