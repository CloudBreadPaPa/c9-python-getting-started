from pathlib import Path
cwd = Path.cwd()

# 상위 디렉토리 참조
parent = cwd.parent

# 디렉토리인지 체크
print('\nIs this a directory? ' + str(parent.is_dir()))

# 파일인지 체크
print('\nIs this a file? ' + str(parent.is_file()))

# 하위 디렉토리 목록 리스트
print('\n-----directory contents-----')
for child in parent.iterdir():
    if child.is_dir():
        print(child)
