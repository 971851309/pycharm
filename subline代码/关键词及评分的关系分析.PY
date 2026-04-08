#将九分以上电影关键词作为索引，记录出现的百分比
import pandas as pd
import pyecharts as pyec
kw_counts_list_by_score = [[] for i in range(10)]
for i in range(4,10):
	kw_counts_list_by_score[i] = pd.read_csv('movie_keywords_by_score/{}_movie_keywords.csv'.formt(i))
	#索引为关键词，列为得分
	kw_percentage_df = pd.DataFrame([],
        cokumns=list(range(4,10)),
        index=kw_counts_list_by_score[9]['kw'][:10]
		)
#筛选数据并填充进DataFrame中
#没有找到关键词填0
for i in range(4,10)
    kw = kw_counts_list_by_score[i]
    kw = kw[kw['kw'].isin(kw_percentage_df.index)]
    kw_percentage_df[i] = Series(list(kw['percentage']),index=kw['kw'])#index表示索引
kw_percentage_df.fillna(0,inplace=True)#implace表示更改原始表格
#一个列表，里面的数据项也是一个列表，数据项由三个数字构成，xyz坐标

data = []
i = 0
for index in kw_percentage_df.index;
     j=0
     for column in kw_percentage_df.columns:
     	  data.append([j,i,kw_percentage_df[column][index]*100])#乘以100，防止数值太小不好观看
     	  j+=1
     i+=1
#绘制热力图
#标记点和标记线
heatmap = pec.HratMap()
heatmap.add("电影评论关键词的热力图",
    kw_percentage_df.columns,
    kw_percentage_df.index,
    data,
    is_visualmap=True,
    visual_text_color="#000",
    visual_range=[0,10],
    visual_orient='horizontal'
    )