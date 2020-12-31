# Python 3.6 이상 필요
# 라이브러리 참조
from pathlib import Path

# 현재 작업 디렉토리 체크
cwd = Path.cwd()
print('\nCurrent working directory:\n' + str(cwd))

# 전체 경로명을 경로(path)와 파일명을 join해 생성 / 출력
new_file = Path.joinpath(cwd, 'new_file.txt')
print('\nFull path:\n' + str(new_file))

# 파일이 존재하는지 체크
print('\nDoes that file exist? ' + str(new_file.exists()) + '\n')