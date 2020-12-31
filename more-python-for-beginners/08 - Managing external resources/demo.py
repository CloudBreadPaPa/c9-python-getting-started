try:
	stream = open('output.txt', 'wt')
	stream.write('Lorem ipsum dolar')
finally:
	stream.close() # 매우 중요한 코드

# with open('output.txt', 'wt') as stream:
# 	stream.write('Lorem ipsum dolar')
