#算法研习社
#加了一个for循环
#第一步，去掉各种标点符号，使之成为列表
def find_word_count(words,words_set):
	words_count = {}#用字典，单词不会重复且要储存答案（即词汇出现的次数）
	for word in words_set:
		words_count[word] = 0
	for word in words:
		words_count[word] += 1
		#if word in words_count:#如果单词已经存在里面，把对应数字加一即可
		##    words_count[word] += 1#如果单词已经存在里面，把对应数字加一即可
		#else:words_count[word] = 1#本身已经是第一个单词，故直接=1
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
print(len(words))#用len函数就知道整个文章有多少单词
words_set = set(words)#去掉重复单词
print(len(words_set))#再看下这个时候还有多少单词
print(find_word_count(words,words_set))#做个词频统计，这里假设已经有find_word_count()函数