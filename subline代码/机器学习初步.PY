#机器学习分类

from sklearn import svm#LinearSVC是SVM的一种
from sklearn.model_selection import train_test_split
#本次的鸢尾花数据为模块自带。
from sklearn import datasets#导入模块，注意：scikit-learn在python中是sklearn
#数据切分
#直接loar_iris()即可获取自带数据
iris = datasets.load_iris()
#print(iris)#输出结果看看
X = iris.data
y = iris.target
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=0)#sklearn.model selection模块的train test split,train test split可将数据分为两个部分，一部分为train，即训练用数据，一部分为test即测试用数据，test size可以调节训练和测试数据比例，random state可以确保切分状态一致
#创建列表的快速方法
easy_list = [i*i for i in range(10)]
print(easy_list)
#只需要循环不需要循环变量时用下划线代替，表示不需要，只是占个位置
for _ in range(10):
	print('Hello makerbean')#这里的目的只是输出十个Hello makerbean


#创建一个LinearSVC分类器
clf = svm.LinearSVC()
clf.fit(X_train,y_train)
#通用流程
#1.创建分类器/回归器等
#2.xxx.fitx(训练数据输入值，对应正确结果)
#3.xxx.predict(待检测数据输入值)



#模型得分
#通过.score()计算模型得分
print('得分:{}'.format(clf.score(X_test,y_test)))#得分=正确数量/数据总数
#通过.predict()预测新数据
y_predict = clf.predict(X_test)
print(y_predict)
print(y_test)



#load_boston()#获取数据
#boston.DESCR获取数据说明
boston = datasets.load_boston()
print(boston.DESCR)