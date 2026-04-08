#多项分布朴素贝叶斯#将结果与target结合起来
#文本数据处理问题
#自然语言处理(NLP)即将机器学习与文本数据处理相结合
#文本的分类
#需要过滤掉的字词即被称为Stop Words(停用词)
#scikit-learn的计数向量转化
from sklearn.feature_extraction.text import CountVectorizer#引入包，用来处理提取文本特征
from sklearn import datasets
from sklearn.feature_extraction.text import TfidfTransformer#scikit-learn中的TF-IDF方法
from sklearn.naive_bayes import MultinomialNB#MultinomialNB--多项分布朴素贝叶斯

count_vext = CountVectorizer(stop_words='english')#与scikit-learn的计数向量转化配套，转化为词频矩阵过滤停用词
#直接fetch_20newsgroups()即可获得新闻数据
data_train = datasets.fetch_20newsgroups(subset='train',remove=('headers','footers','quotes'),
)#subset='train'参数，意为获取一部分,再利用remove参数移走不需要的部分，这里去除了帖子的头尾，只保留正文内容
count_vect = CountVectorizer(stop_words='english')
X_train_counts = count_vect.fit_transform(data_train.data)#数据统计转换
tfidf_transformer = TfidfTransformer().fit(X_train_counts)
X_train_tfidf = tfidf_transformer.transform(X_train_counts)
text_test = ['Do you use Mac','God loves you','OpenGL on the GPU is fast']
X_test_counts = count_vect.transform(text_test)#统计词频
X_test_tfidf = tfidf_transformer.transform(X_test_counts)#计算TF-IDF值
clf = MultinomialNB().fit(X_train_tfidf,data_train.target)
predicted = clf.predict(X_test_tfidf)
#将结果与target结合起来
for doc,category in zip(text_test,predicted):
	print('{}--------> {}'.format(doc,data_train.target_names[category]))
print(data_train.data[0])
print(type(data_train.data[0]))#看下数据是什么类型
print(data_train.target_names)#查看都有哪些分类名称
print(data_train.target_names[data_train.target[0]])#查看一篇文章对应的分类
#对应文本分类的基本原理：根据文章常出现的词语来确定分类
print(X_train_counts.shape)
print(X_train_tfidf.shape)
print(predicted) 




