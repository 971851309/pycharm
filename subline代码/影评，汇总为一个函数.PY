#词云老版本函数构造，理解思路
def generate_word_cloud(world_list,path_name):
	wordcloud = pec.WordCloud(width=1300,height=620)
	wordcloud.add("",word_list.index,word_list.values
		word_size_range=[20,100],
		shape='diamond')
	wordcloud.render(path=path_name)
	print('Generate word cloud file done:{}'.format)


#调用函数的方法
path_name = 'wordcloud/{}_{}.html'.format(movie_name)
generate_word_cloud(word_list,path_name)


