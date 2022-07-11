'''
@author king_xiong
@date 2022-03-06 16:29
'''
import graphviz
import pandas as pd

from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import train_test_split
from sklearn.tree import export_graphviz, DecisionTreeClassifier

if __name__ == '__main__':
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

    # 3.划分数据集
    x_train,x_test,y_train,y_test =train_test_split(x,y,random_state=22)

    # 4.字典特征抽取
    transfer=DictVectorizer()
    x_train=transfer.fit_transform(x_train)
    x_test=transfer.transform(x_test)

    # 3)决策树预估器 选择entropy信息熵类别
    estimator = DecisionTreeClassifier(criterion="entropy",max_depth=8)
    estimator.fit(x_train, y_train)

    # 4)模型评估
    y_predict = estimator.predict(x_test)
    score = estimator.score(x_test, y_test)
    print("y_predict:\n", y_predict)
    print("y_test==y_predict:\n", y_test == y_predict)
    print("score:\n", score)

    # 5）可视化数据
    dot_data = export_graphviz(estimator,
                               out_file=None,
                               feature_names=transfer.get_feature_names(),
                               filled=True,  # 填充决策树颜色
                               rounded=True, )  # 决策树的圆角
    graph = graphviz.Source(dot_data.replace("helvetica", "FangSong"))  # 如果乱码就加上这个
    # graph=graphviz.Source(dot_data)
    graph.view()

