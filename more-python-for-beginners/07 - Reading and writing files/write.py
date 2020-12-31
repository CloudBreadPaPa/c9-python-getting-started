# 쓰기 작업을 하기 위해 output.txt를 텍스트 파일로 열고 객체를 가져옴
stream = open('output.txt', 'wt')

print('\nCan I write to this file? ' + str(stream.writable()) + '\n')

stream.write('H') # 한줄 문자열 작성 
stream.writelines(['ello',' ','world']) # 여러줄의 문자열 작성
stream.write('\n') # 새줄(new line) 작성

names = ['Susan','Christopher']
stream.writelines(names)

# 리스트의 각 항목 사이에 새줄을 추가하는 깔끔한 방법
stream.write('\n')  # 새줄 작성
stream.writelines('\n'.join(names)) 
stream.close() # 파일 스트림을 flush하고 close
