from sklearn import svm#LinearSVC是SVM的一种
from sklearn.model_selection import train_test_split
#本次的鸢尾花数据为模块自带。
from sklearn import datasets#导入模块，注意：scikit-learn在python中是sklearn
import pyecharts as pec
from pyecharts.charts import Scatter



#load_boston()#获取数据
#boston.DESCR获取数据说明
boston = datasets.load_boston()
print(boston.DESCR)

#绘制散点图直观感受数据分布
scatter_list = []
for i in range(13):
	scatter = pec.Scatter(boston.feature_names[i],
		title_pos='center')
	scatter.add('',boston.data[:,i],boston.target)
	scatter_list.append(Scatter)
page = pec.Page()
for i in range(13):
	page.add(scatter_list[i])
page.render(path='scatter by feature.html')

#切分为训练数据集和测试数据集
X = boston.data
y = boston.target
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=)
#判断属于回归类算法
#导入模块先
from sklearn import linear_model
#创建回归器并训练
lasso = linear_model.Lasso()
lasso.fit(X_train,y_train)
#引入均方差
from sklearn.metrics import mean_squared_error
mse = mean_squared_error(y_test,lasso.predict(X_test))
score = lasso.score(X_test,y_test)
print('MSE:{}'.format(mse))
print('Score:{}'.format(score))
#调节参数
lasso = linear_model.Lasso(alpha=0.1)#具体参数参考官方文档


#利用scikit-learn的网格搜索调节参数
from sklearn.model_selection import GridSearchCV
alpha_range = np.alpha_range(0,1,0.05)#要调整的alpha值的参数
param_grid = {'alpha':alpha_range}#将参数名称写入''冒号后为参数值的列表
lasso_search = GridSearchCV(lasso,param_grid)#用GridSearchCV函数写入要调整的模型lasso及该模型的参数param_grid
lasso_search.fit(X_train,y_train)#直接使用模型训练
for result in lasso_search.cv_results_:#输出最好的数值
	print(result,lasso_search.cv_results_[result])
print(lasso_search.best_score_)
print(lasso_search.best_params_)
print(lasso_search.best_estimator_)
#各个回归模型都可以测试一下
lasso = linear_model.Lasso()
eln_reg = linear_model.ElasticNext()
svr_reg = svm.SVR()
nusvr_reg = svm.NuSVR()
ridge_reg = linear_model.Ridge()
gbr_reg = ensemble.GradientBoostingRegressor()
#查看各个特征的重要程度
feature_importance_df = pd.DataFrame({
	'name':boston.feature_names,
    'importance':gbr_reg.feature_importance_
	})
feature_importance_df.sort_values(by='importance',ascending=False,inplace=True)
bar = pec.Bar('各特征重要性',width=1280,height=720)
bar.add('',feature_importance_df.name,feature_importance_df.importance)
bar.render(path='各特征重要性.html')



#利用随机搜索来降低搜索复杂度
#注意添加n_iter=测试次数，确定需要测试的次数
n_estimators_range = np.arange(100,1000,100)
max_depth_range = np.arange(3,10)
learning_rate_range = [0.0001,0.001,0.01,0.1]#调整三个参数
param_grid = {
        'n_estimators':n_estimators_range,
        'max_depth':max_depth_range,
        'learning_rate'	:learning_rate_range
}
gbr_search = RandomizedSearchCV(gbr_reg,param_grid,n_iter=30)#n_iter表示随机多少次
gbr_search.fit(X_train,y_train)
for result in gbr_search.cv_results_:
	print(result)
print(gbr_search.best_score_)
print(lasso_search.best_params_)
print(lasso_search.best_estimator_)
