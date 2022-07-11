'''
@author king_xiong
@date 2022-03-05 17:38
'''
import pandas as pd
# 1.读取数据
# 读取文件使用绝对路径时 要用/
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
if __name__ == '__main__':
    data = pd.read_csv("F:/some_learning_materials/机器学习\Machine_Learning/resources/FBlocation/train.csv")
    # print(data)
    # print(data.head())
    # 2.基本数据处理
    # 1）缩小数据范围

    data=data.query("x < 3 & x >1.5 & y<1.5 & y > 1.0 ")

    # print(data)
    # 2）处理时间特征
    time_value =pd.to_datetime(data["time"],unit="s")
    date=pd.DatetimeIndex(time_value)
    data["day"]=date.day
    data["weekday"]=date.weekday
    data["hour"]=date.hour
    # 3)过滤掉签到次数比较少的地点
    # print(data.groupby("place_id").count())
    place_count = data.groupby("place_id").count()["row_id"]
    # print(place_count)
    data_final=data[data["place_id"].isin(place_count[place_count>3].index.values)]
    # print(data_final)
    # 4)筛选特征值和目标值
    x =data_final[["x","y","accuracy","day","weekday","hour"]]
    y =data_final["place_id"]
    # 3.数据集划分
    x_train,x_test,y_train,y_test=train_test_split(x,y)
    print(x_train)

    # 4.特征工程 标准化
    transfer=StandardScaler()
    x_train=transfer.fit_transform(x_train)

    # 保证相同的平均值和标准差
    x_test=transfer.transform(x_test)
    # KNN算法预估器
    estimator=KNeighborsClassifier(n_neighbors=3)
    estimator.fit(x_train,y_train)

    # 5.加入网格搜索和交叉验证
    # 准备参数 调整超参数 cv代表交叉验证的次数
    params_dict={"n_neighbors":[3,5,7]}
    estimator=GridSearchCV(estimator,param_grid=params_dict,cv=5)
    estimator.fit(x_train,y_train)

    # 6.模型评估
    y_predict=estimator.predict(x_test)
    score=estimator.score(x_test,y_test)
    print("y_predict:\n",y_predict)
    print("y_test==y_predict:\n",y_test==y_predict)
    print("score:\n",score)