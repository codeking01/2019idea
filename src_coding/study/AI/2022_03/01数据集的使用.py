'''
@author king_xiong
@date 2022-03-04 15:20
'''
from sklearn import datasets
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

def datasets_demo():
    '''
    sklearn数据集的使用
    :return:
    '''
    # 加载小规模数据集
    iris = load_iris()

    # 获取大规模数据 加载小规模数据集 还可以用 var = datasets.load_ * ()
    # data=datasets.fetch_*(data)
    # 返回值是一个继承字典的Bench 特性：它有自己的键值对

    print("鸢尾花数据集：\n",iris)
    print("查看数据集描述：\n",iris["DESCR"])
    print("查看特征值的名字：\n",iris.feature_names)
    print("查看特征值：\n",iris.data,iris.data.shape)

    # 数据集划分 iris.data(特征值),iris.target（目标值），test_size=0.2 是20%做测试集，random_state是随机树种子
    x_train,x_test,y_train,y_test =train_test_split(iris.data,iris.target,test_size=0.2,random_state=22)
    print("训练集的特征值：\n",x_train,x_train.shape)
    return None

if __name__ == '__main__':
    datasets_demo()