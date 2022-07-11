'''
@author king_xiong
@date 2022-03-07 10:45
'''
from sklearn import svm
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, GridSearchCV


def SVM_demo():
    '''
    支持向量机SVM
    :return:
    '''

    # 1.获取数据
    iris =load_iris()
    # 查看键值
    # iris.keys()
    # 划分数据集
    x_train,x_test,y_train,y_test =train_test_split(iris.data,iris.target,test_size=0.25,random_state=3)

    # 建模
    # kernel核函数 把低纬数据换成高纬度数据 使得数据集更好的划分 高斯核函数RBF  gamma 为超参数
    # Gamma是用于非线性支持向量机的超参数。最常用的非线性核函数之一是径向基函数(RBF)。RBF的Gamma参数控制单个训练点的影响距离。
    # gamma值较低表示相似半径较大，这会导致将更多的点组合在一起。对于gamma值较高的情况，点之间必须非常接近，才能将其视为同一组(或类)。因此，具有非常大gamma值的模型往往过拟合。
    # 惩罚因子C越大时，被误分类的样本点的个数就越小。
    estimator=svm.SVC(C=2,kernel='rbf',gamma=10,decision_function_shape='ovr')
    estimator.fit(x_train,y_train.ravel())

    #加入网格搜索和交叉验证
    # 准备参数 调整超参数 cv代表交叉验证的次数
    params_dict = {'C':[1e1,1e2,1e3, 5e3,1e4,5e4],
                  'gamma':[0.0001,0.0008,0.0005,0.008,0.005,]}
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


if __name__ == '__main__':
    SVM_demo()