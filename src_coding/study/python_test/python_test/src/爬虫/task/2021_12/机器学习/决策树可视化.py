import pydotplus
from IPython.core.display import Image
from sklearn import tree
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
import pandas as pd
import graphviz

wine = load_wine()
Xtrain, Xtest, Ytrain, Ytest = train_test_split(wine.data, wine.target, test_size=0.3)
# print(Xtrain.shape)   # 输出训练集的形状
# print(Xtest.shape)

clf = tree.DecisionTreeClassifier(criterion='entropy') # 实例化
clf = clf.fit(Xtrain, Ytrain)
score = clf.score(Xtest, Ytest)  # score 指的是预测准确度
print(score)

feature_name = ['酒精', '苹果酸', '灰', '灰的碱性', '镁', '总酚', '类黄酮', '非黄烷类酚类', '花青素', '颜色强度', '色调', 'od280/od315稀释葡萄酒', '脯氨酸']
dot_data = tree.export_graphviz(clf
                                , feature_names=feature_name
                                , class_names=['琴酒', '雪莉', '贝尔摩德']
                                , filled=True
                                , rounded=True
                                )
graph = graphviz.Source(dot_data)
graph=graphviz.Source(dot_data.replace("helvetica","FangSong")) #如果乱码就加上这个
graph.view()
# 同级目录下生成pdf文件
graph.render('tree')
# graph.view() #查看决策树