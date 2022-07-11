from sklearn import tree
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split

wine = load_wine()  # 这个是一个字典
# print(wine)
# print(wine.data.shape)
# print(wine.target)
# 如果wine是一张表，应该长这样：
import pandas as pd
pd.concat([pd.DataFrame(wine.data),pd.DataFrame(wine.target)],axis=1)
# print(wine.target_names)
# # 0.3做测试集  剩下的做训练集
Xtrain, Xtest, Ytrain, Ytest = train_test_split(wine.data,wine.target,test_size=0.3)
print(Xtrain.shape)
clf = tree.DecisionTreeClassifier(criterion="entropy"
                                  ,random_state=30
                                  ,splitter="best"  #输入“random"，决策树在分枝时会更加随机，树会因为含有更多的不必要信息而更深更大，并因这些不必要信息而降低对训练集的拟合。这也是防止过拟合的一种方式。当你预测到你的模型会过拟合，用这两个参数来帮助你降低树建成之后过拟合的可能性。当然，树一旦建成，我们依然是使用剪枝参数来防止过拟合。
                                  # ,max_depth=3  #限制树的最大深度，超过设定深度的树枝全部剪掉
                                  # ,min_samples_leaf=10 # 限制树的最大深度，超过设定深度的树枝全部剪掉
                                  # ,min_samples_split=10 #一个节点必须要包含至少min_samples_split个训练样本，这个节点才允许被分枝，否则分枝就不会发生。
                                  )
clf = clf.fit(Xtrain, Ytrain)
score = clf.score(Xtest, Ytest) #返回预测的准确度
print(score)
feature_name = ['酒精','苹果酸','灰','灰的碱性','镁','总酚','类黄酮','非黄烷类酚类','花青素','颜色强度','色调','od280/od315稀释葡萄酒','脯氨酸']
import graphviz
dot_data = tree.export_graphviz(clf
                                ,out_file = None
                                ,feature_names= feature_name
                                ,class_names=["琴酒","雪莉","贝尔摩德"]
                                ,filled=True    #填充决策树颜色
                                ,rounded=True    #决策树的圆角
                                )
# graph = graphviz.Source(dot_data)
graph=graphviz.Source(dot_data.replace("helvetica","FangSong")) #如果乱码就加上这个
graph.view()
# 探索特征的重要性
# print(clf.feature_importances_)
# print(*zip(feature_name,clf.feature_importances_))
# score_train = clf.score(Xtrain, Ytrain)
# print(score_train)
import matplotlib.pyplot as plt
test = []
for i in range(10):
    clf = tree.DecisionTreeClassifier(max_depth=i+1
                                      ,criterion="entropy"
                                      ,random_state=30
                                      ,splitter="random"
                                      )
    clf = clf.fit(Xtrain, Ytrain)
    score = clf.score(Xtest, Ytest)
    test.append(score)
plt.plot(range(1,11),test,color="red",label="max_depth")
plt.legend()
plt.show()

# 所有接口中要求输入X_train和X_test的部分，输入的特征矩阵必须至少是一个二维矩阵。sklearn不接受任何一维矩阵作为特征矩阵被输入
clf.apply(Xtest)
clf.predict(Xtest)