'''
@author king_xiong
@date 2022-03-06 11:40
'''
import graphviz
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_graphviz


def decsion_tree():
    '''
    决策树
    :return:
    '''
    # 1)获取数据
    iris = load_iris()
    # 2)数据集划分
    x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, random_state=22)
    # 3)决策树预估器 选择entropy信息熵类别
    estimator = DecisionTreeClassifier(criterion="entropy")
    estimator.fit(x_train, y_train)

    # 4)模型评估
    y_predict = estimator.predict(x_test)
    score = estimator.score(x_test, y_test)
    print("y_predict:\n", y_predict)
    print("y_test==y_predict:\n", y_test == y_predict)
    print("score:\n", score)

    # 5）可视化数据
    dot_data = export_graphviz(estimator,
                               out_file="iris_tree.dot",
                               feature_names=iris.feature_names,
                               # class_names=["琴酒", "雪莉", "贝尔摩德"],
                               filled=True,  # 填充决策树颜色
                               rounded=True, )  # 决策树的圆角
    graph = graphviz.Source(dot_data.replace("helvetica", "FangSong"))  # 如果乱码就加上这个
    graph.view()
    return None


if __name__ == '__main__':
    decsion_tree()
