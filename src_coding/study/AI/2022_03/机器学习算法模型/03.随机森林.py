'''
@author king_xiong
@date 2022-03-06 19:24
'''
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import train_test_split, GridSearchCV


def random_forest():
    '''
    随机森林 验证泰坦尼克号
    :return:
    '''
    # 1.获取数据
    titanic=pd.read_csv("F:/some_learning_materials/机器学习/Machine_Learning/resources/titanic/titanic.csv")
    # print(titanic)
    # 筛选特征值和目标值
    x=titanic[["pclass","age","sex"]]
    y=titanic["survived"]
    # 2.数据处理
    # 1）缺失值处理
    x["age"].fillna(x["age"].mean(),inplace=True)
    # print(x)
    # 2)转化成字典
    x=x.to_dict(orient="records")
    print(x)

    # 3.划分数据集
    x_train,x_test,y_train,y_test =train_test_split(x,y,random_state=22)

    # 4.字典特征抽取
    transfer=DictVectorizer()
    x_train=transfer.fit_transform(x_train)
    x_test=transfer.transform(x_test)

    estimator=RandomForestClassifier()
    # 加入网格搜索和交叉验证
    # 参数准备
    params_dict={"n_estimators": [120,200,300,500,800,1200],"max_depth": [5, 8, 15, 25, 30]}
    estimator=GridSearchCV(estimator,param_grid=params_dict,cv=3)
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
    return None

if __name__ == '__main__':
    random_forest()