presenters = [
    {'name': 'Susan', 'age': 50},
    {'name': 'Christopher', 'age': 47}
]

# 알파벳 순으로 정렬
presenters.sort(key=lambda item: item['name'])
print('-- alphabetically --')
print(presenters)

# name의 길이로 정렬(짧은것부터 긴것까지)
presenters.sort(key=lambda item: len(item['name']))
print('-- length --')
print(presenters)
