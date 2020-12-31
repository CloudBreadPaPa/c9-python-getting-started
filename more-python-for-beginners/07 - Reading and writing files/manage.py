# 텍스트 쓰기 작업을 위해 manage.txt 파일 객체를 가져옵니다.
stream = open('manage.txt', 'wt')

# 파일스트림에 demo 단어를 작성
stream.write('demo!')

# 파일스트림의 시작 위치로 이동
stream.seek(0)

# cool 단어를 파일시스템에 작성
stream.write('cool')

# 파일 버퍼로 파일스트림 콘텐트를 flush(플러시)
stream.flush()

# 파일스트림을 flush하고 파일 close
stream.close()
