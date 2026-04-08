#整理数据
#导入pyecharts并绘制词云图
#列表前加~表示取反
#方案二，建立关键词过滤列表
#进一步改进为方便调用函数的式样
#电影评论的数据处理
#观察每行有什么数据
#导入sqlite3和pandas 
import sqlite3
import pandas as pd
import jieba
import pyecharts as pec
import math
FILTER_WORDS=['知道','影评','电影','影片','这么','那么','怎么','如果','\n','一部','这部','没有','还有']#根据实际情况来调整过滤词列表，具体问题具体分析。
##设计为函数，方便调用
def get_movie_id_list(min_comment_count):
	movie_list = comment_data['MOVIEID'].value_counts()
	movie_list = movie_list[movie_list.values>min_comment_count]
	return movie_list.index#返回ID的值而不是这个ID初现了多少次
	#筛选出前十个评论里最多的关键词
def  get_comment_keywords_counts(movie_id,count):
	 comment_list = comment_data[comment_data['MOVIEID']==movie_id]['CONTENT']
	 comment_str_all = ''
	 for comment in comment_list:
		 comment_str_all += comment + '\n'
	 seg_list = list(jieba.cut(comment_str_all))
	 #转换成Pandas的Series类型数据
	 keywords_counts = pd.Series(seg_list)
	 #利用str.len()筛选字符串长度
	 keywords_counts = pd.Series(seg_list)
	 keywords_counts = keywords_counts[keywords_counts.str.len()>1]

	 return keywords_counts
#写为函数方便调用	 
def get_movie_name_and_score(movie_id):
	   #根据电影ID在douban_movie_data找出电影名和评分
	#douban_movie_data中体现ID的是链接
	movie_link = 'https://movie.douban.com/subject/{}/'.format(movie_id)
	
	search_result = movie_data[movie_data['链接']==movie_link].iloc[0]#只把第一行的内容给筛选出来，通过".iloc[0]"
	movie_name = search_result['电影名']
	movie_score = search_result['评分']
	return(movie_name,movie_score)


#词云老版本函数构造，理解思路
def generate_word_cloud(world_list,path_name):
	wordcloud = pec.WordCloud(width=1300,height=620)
	wordcloud.add("",word_list.index,word_list.values
		word_size_range=[20,100],
		shape='diamond')
	wordcloud.render(path=path_name)
	print('Generate word cloud file done:{}'.format)

#连接数据库并读取表格
conn = sqlite3.connect('douban_comment_data.db')#填入文件路径，此处把读取所需文件与代码放在了一起
comment_data = pd.read_sql_query('select*from comment;',conn)
movie_data = pd.read_excel('douban_movie_data.xlsx')


movie_id = '1292052'
keywords_counts = get_comment_keywords_counts(movie_id,30)#取前30个关键词
wordcloud = pec.WordCloud(width=1280,height=720)
wordcloud.add("",keywords_counts.index,keywords_counts.values,
	word_size_range=[20,100],
	shape='diamond')
wordcloud.render()
movie_name,movie_score = get_movie_name_and_score(movie_id)

#调用函数的方法
path_name = 'wordcloud/{}_{}.html'.format(movie_name,movie_score)
generate_word_cloud(word_list,path_name)
generate_word_cloud(keywords_counts,path_name)


#关键词及评分的关系分析
#以电影评论关键词作为切入
#展示与评分的联系
#不同评分下的关键词还具有不同的热度
#所以，一共有几个维度的数据三个维度，可用3D柱状图和热力图展示1，不同的关键词，2不同的打分，3，不同的关键词在不同的打分下还有不同的热度。
#创建两个列表，存储关键词和出现次数把每部电影的30个关键词按评分区间放进去
#每个列表都含十个列表
kw_list_by_score = [[]for _ in range(10)]
kw_counts_list_by_score = [[] for _ in range(10)]
#每个列表都含有十个列表
movie_id_list=get_movie_id_list(300)
for movie_id in movie_id_list:
      word_list = get_comment_kw_counts(movie_id,30)
      movie_name,movie_score=get_movie_name_and_score(movie_id)
      try:
      	  
      	  kw_counts_list_by_score[math.floor(movie_score)].extend(word_list.index)#通过extend，把列表movie_score加进word_list
      	  kw_list_by_score[math.floor(movie_score)].extend(word_list.values)
      except:
      	  print(movie_id)

#每次创建一个DataFrame数据
#保存该得分区间的TOP3-关键词和出现总次数
for i in range(10)
    if kw_list_by_score[i]:
    	kw30_with_counts = pd.DataFrame({
             'kw': kw_list_by_score[i],
             'counts': kw_counts_list_by_score[i]
    		})


#统计关键词的出现总次数，并算出百分比，并储存为文件
kw30_with_counts = kw30_with_counts.groupby('kw').sum()
kw30_with_counts = kw30_with_counts.sort_values(by='counts',ascending=False)[:30]#第一步，通过sort_values按照计算次数（counts）来排序，再通过ascending=False进行降序排列
counts_sum = kw30_with_counts['counts'].sum()#将每部电影前30位关键词取出来后，把它们打分的次数进行求和（相当于按比例显示）
kw30_with_counts['percentage'] = kw30_with_counts['counts']/counts_sum
kw30_with_counts.to_csv('movie_keywords_by_score/{}_movie_keywords.csv'.format(i))#将其存入一个CSV文件
















