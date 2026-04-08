#算法研习社
#第一步，去掉各种标点符号，使之成为列表
words = []
with open('同一目录下的文件名','r') as f:
	lines = f.readlines()
	for line in lines:
		line = line.replace(',','')
		line = line.replace('.','')
		line = line.replace('"','')
		line = line.replace('!','')
		line = line.replace('?','')
		line = line.replace(':','')
		line = line.replace('\'','')#注意如果要分离'用的斜杠
		line = line.replace('-','')
		line = line.replace('\n','')
		for word in line.split(''):
			if word:
				words.append(word)
print(words)