'''
@author king_xiong
@date 2022-03-05 14:24
'''
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

if __name__ == '__main__':
    # 获取数据
    iris =load_iris()
    # 划分数据集
    x_train,x_test,y_train,y_test =train_test_split(iris.data,iris.target,test_size=0.25,random_state=3)
    # 特征工程 标准化
    transfer=StandardScaler()
    x_train=transfer.fit_transform(x_train)

    # 保证相同的平均值和标准差
    x_test=transfer.transform(x_test)
    # KNN算法预估器
    estimator=KNeighborsClassifier(n_neighbors=3)
    estimator.fit(x_train,y_train)

    #加入网格搜索和交叉验证
    # 准备参数 调整超参数 cv代表交叉验证的次数
    params_dict={"n_neighbors":[1,3,5,7,9,11]}
    estimator=GridSearchCV(estimator,param_grid=params_dict,cv=10)
    estimator.fit(x_train,y_train)

    # 模型评估
    y_predict=estimator.predict(x_test)
    score=estimator.score(x_test,y_test)
    print("y_predict:\n",y_predict)
    print("y_test==y_predict:\n",y_test==y_predict)
    print("score:\n",score)
    print('-----')
    print("最佳参数：\n",estimator.best_params_)
    print("最佳结果：\n",estimator.best_score_)
    print("最佳预估器：\n",estimator.best_estimator_)
    print("最佳交叉验证结果：\n",estimator.cv_results_)