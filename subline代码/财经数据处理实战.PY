#导入tushare模块
#去掉名字，领域，地域
#分类
import tushare as ts
from sklearn.cluster import MeanShift,estimate_bandwidth
from sklearn.cluster import KMeans
#去掉名字，领域，地域
stock_df = ts.get_hs300s()#沪深（简短信息）
stock_basics = ts.get_stock_basics()#找出详细信息
stock_basics = stock_basics.loc[stock_df['code'].values]
X = stock_basics.drop(['name','industry','area'],1)
bandwidth = estimate_bandwidth(X)
ms = MeanShift(bandwidth=bandwidth,bin_seeding=True)#MeanShift聚类
ms.fit(X)
#print(stock_df)
#print(stock_basics)
#再利用pandas筛选数据
#print(stock_basics)
labels = ms.labels_
for company,label in zip(stock_basics['name'],labels):
	print(f'{company}-->{label}')

