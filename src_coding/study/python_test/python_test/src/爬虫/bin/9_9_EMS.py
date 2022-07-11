stu=['\t熊嘉亮\t21\t\t湖南'] # 这个地方需要暂时用字符串存储
while True :
        print('*'*20,'欢迎使用EMS系统','*'*20)
        print("\t1.查询员工")
        print("\t2.添加员工")
        print("\t3.删除员工")
        print("\t4.退出系统")
        user_choose=input("请选择（1-4）进行操作: ")
        print('*'*62)
        if user_choose=='1' : #查询
                print("\t序号\t姓名\t年龄\t地址")
                for s in stu :
                        n=1
                        print(f'\t{n}\t{s}')
                        n+=1
        elif user_choose=='2' :  #添加
                add_user=input("请输入名字，年龄，地址: ")
                stu.extend(add_user)
        elif user_choose=='3':  #删除
                print("开始查询吧")
        elif user_choose=='4' :  #退出
               input("欢迎使用此系统，再见，使用回车键结束程序！")
               break
        else :
               print("输入错误！请你重新选择！")
        print('*'*62)
else :
        print("输入错误，重新输入")