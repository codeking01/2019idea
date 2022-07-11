import pymysql

import os

path = "../3D_pic"  # 文件夹目录
files = os.listdir(path)  # 得到文件夹下的所有文件名称 (是列表类型)

# for i in range(len(files)):
# 打开数据库连接
db = pymysql.connect(host="localhost", user="root", password="123456", database="pubimage")
# 使用cursor（）方法获取游标
cursor = db.cursor()
# 执行SQL语句
# fp = open("./3D_pic/"+str(files[i]),'rb')
# img = fp.read()
# fp.close()
#
# insert_sql = "insert into test01(image) values(%s)"
# parm=(img)
# 执行sql语句
# cursor.execute(insert_sql,parm)
# 提交到数据库执行
# db.commit()
cursor.execute("select id,cas from test01")
# 查看表里所有数据
data = cursor.fetchall()
# print(type(data))
print(data)
print(len(data))
print(data[0][1])
# for i in data:
#     print(data[1])

# 关闭游标
cursor.close()
# 关闭数据库连接
db.close()
