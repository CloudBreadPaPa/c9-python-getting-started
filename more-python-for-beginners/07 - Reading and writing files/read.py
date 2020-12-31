# demo.txt 파일을 열고, 내용을 읽음
stream = open('./demo.txt', 'rt')
print('\nIs this readable? ' + str(stream.readable()))
print('\nRead one character : ' + stream.read(1))
print('\nRead to end of line : ' + stream.readline())
print('\nRead all lines to end of file :\n' + str(stream.readlines())+ '\n')