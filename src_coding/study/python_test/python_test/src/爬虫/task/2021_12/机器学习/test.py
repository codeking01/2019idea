import graphviz
from sklearn import tree
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split

wine = load_wine()

Xtrain, Xtest, Ytrain, Ytest = train_test_split(wine.data, wine.target, test_size=0.3)

clf = tree.DecisionTreeClassifier(criterion='entropy'
                                  ,random_state=30
                                  ,splitter='random')
# random_state随机模式可输入任意数字，
cl = clf.fit(Xtrain, Ytrain)
score = clf.score(Xtest, Ytest)
print(score)

feature_name = ['酒精', '苹果酸', '灰', '灰的碱性', '镁', '总酚', '类黄酮', '非黄烷类酚类', '花青素', '颜色强度', '色调', 'od280/od315稀释葡萄酒',
                '脯氨酸']  # 特征值
dot_data = tree.export_graphviz(
    clf,
    feature_names=feature_name,
    class_names=['琴酒', '雪梨', '贝尔摩德'],
    filled=True,  # 是否填充颜色，true 填充颜色
    rounded=True,  # 框的形状
)
graph = graphviz.Source(dot_data)  # 此行代码出现问题！！！
graph.render('wine_tree')
