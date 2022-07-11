# str='1<d class=\"num\">&#xe44a;</d><d class=\"num\">&#xf26a;</d>'  #len=5  107yuan
# # str=str.split('>')
# a=str.split('>')[1].split(';')[0]   #处理100的情况
# print(a)
# b=str.split('>')[3].split(';')[0]
# print(b)

# 处理101
# obj='1<d class=\"num\">&#xe44a;</d>'  #len=3  121 yuan
# obj='<d class=\"num\">&#xf5d6;</d><d class=\"num\">&#xeedb;</d><d class=\"num\">&#xf26a;</d>'
# d=str.split('>')
# print(d)

import requests
import json
import xlwt

# url='http://www.dianping.com/shop/H9Vnbc8KMYG56vZN'
# url = 'http://www.dianping.com/ajax/json/shopDynamic/reviewAndStar?shopId=H9Vnbc8KMYG56vZN&cityId=344&mainCategoryId=34246&_token=eJxVj1tvgkAQhf%2FLPG%2B4LLvLJemDpo2gbtsgUKHxQVaqREFkKdg2%2Fe9dU%2FrQp3Pmm3OSmS9ogx14pmEYxETQFy14YGqGxgBBJ9WGWZS42LKxTWwE4h%2BzCHUR5G1yD96rSS2GMHE2NxIq8EscRjZotFhZTNBNIA9UBA5d13i6PgyDtiu3dVPWe02cK10ezo3uu0mdC2fB0xllffaoTgLVrCLVVHocdTtq9zdz9YPKynJfK1fMr9FKEnl5C7mMYswTfxmJTy4MIlex9bwkQTDLqvQSJjWdislTyF7S9Wn%2BEeZF3%2FjvTZWd4jVdTKYYPxzTO%2Fj%2BAe7EVpU%3D&uuid=751dd7ad-f61c-e41b-0401-95d1866ae493.1634227745&platform=1&partner=150&optimusCode=10&originUrl=http%3A%2F%2Fwww.dianping.com%2Fshop%2FH9Vnbc8KMYG56vZN'
# url = 'http://www.dianping.com/ajax/json/shopDynamic/reviewAndStar?shopId=H9Vnbc8KMYG56vZN&cityId=344&mainCategoryId=34246'
url = 'http://www.dianping.com/ajax/json/shopDynamic/reviewAndStar?shopId=l6c49QrTQEWGFItd&cityId=344&mainCategoryId=34237'
# http://www.dianping.com/ajax/json/shopDynamic/reviewAndStar?shopId=H8UXvXC8OtFaOFcl&cityId=344&mainCategoryId=34245&_token=eJx1j09vgkAQxb%2FLnDewC8uCJD1olUoroUFAbeMBVwVS%2Fsmi2Db97l1Teuihp9%2BbN5N5M5%2FQunuwCcaYEgSXQws2EAUrDBB0QnaYbtCRZYyYSRkC%2Fsczqakh2LXxFOxXYugMEQNvb04gjR%2FHYnSLBqlJqVF0A%2BxcOQJZ1zW2qvZ9r%2BzzpGryKlV4Xaoiqxt1bkXry%2Fre8jsn8R1eyJP%2Bm%2BdZUqUiS6QgWE0JMUFmlKHMkHwbmAzsfmtPfiu3ijytpDo8XsOloOJ0DDwRRpoXzxch%2F%2FA4pmIZ6c8L6roPL%2BXmlMWVMeFjP6CrOnCKGacrNY%2FP%2BdE4v4fF03jCprN6cwdf35whZUQ%3D&uuid=751dd7ad-f61c-e41b-0401-95d1866ae493.1634227745&platform=1&partner=150&optimusCode=10&originUrl=http%3A%2F%2Fwww.dianping.com%2Fshop%2FH8UXvXC8OtFaOFcl
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
    'Cookie': 'navCtgScroll=0; _lxsdk_cuid=17c7f907122c8-005a3d1714b78c-b7a1438-144000-17c7f907122c8; _lxsdk=17c7f907122c8-005a3d1714b78c-b7a1438-144000-17c7f907122c8; _hc.v=751dd7ad-f61c-e41b-0401-95d1866ae493.1634227745; s_ViewType=10; ua=dpuser_15059620632; ctu=1dc952f673738fa47d20413160405840235920484dc849760c4a66b318dd0f6b; fspop=test; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1634227745,1635433785,1635434475; cy=344; cye=changsha; thirdtoken=41702c09-7086-430b-ab15-e7448c57e6c0; dper=234cb94f92704aef13a7e6c816ada0ec5d82dfce20785f8f7461236e5ad4452e080a2eb9d7089f0779c7dccdb93f453054a0e3dd272f57e46cf3f29951cb4adf5159c53995424956e2bae8b3aa6d15febd25ed5e382eabe35e43e4007f6a7b94; ll=7fd06e815b796be3df069dec7836c3df; ctu=b58a9fce079b27059480a633b27a83c81b97ef52648306836b7b2a7e61a47c0127548a04b35974cf992382a35b6cbb17; dplet=7a0ee364bff4bc2bf9ed9183621d7340; _lxsdk_s=17cc773261d-562-249-600%7C%7C710; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1635436153'
}

response = requests.get(url=url, headers=headers)
content = response.text
# with open('1.json','w',encoding='utf-8')as fp:
#     fp.write(content)

dic = {'&#xe44a':'0','&#xe3fc':'1','&#xf5d6':'2','&#xeedb':'3','&#xe807':'4','&#xe8c9':'5','&#xe836':'6','&#xf26a':'7','&#xf447':'8','&#xe405':'9','.1':'1','1':1,}
# items=soup.find_all(class_='brief-info')
obj = json.loads(content)
print(obj)
lenth= len(obj["avgPrice"].split('>'))
obj_price=obj["avgPrice"]

if(lenth==3):
    b=obj_price.split('>')[1].split(';')[0]
    b=dic[b]
    # 要加‘1’
    if(obj_price[0]=='1'):
        if(obj_price[-1]=='1'):#处理101的情况
            price='1'+b+'1'+'元'
        #处理110
        elif(obj_price[1]==1):
            price='11'+b+'元'
        else:
            price='1'+b+'元'
    elif(obj_price[-1]==1):#处理011
        price=b+'11'+'元'
    else:#处理个位数情况
        price=b+'元'
elif(lenth==5):
    # ['<d class="num"', '&#xf5d6;</d', '<d class="num"', '&#xf5d6;</d', '']
    a=obj_price.split('>')[1].split(';')[0]
    a=dic[a]
    b=obj_price.split('>')[3].split(';')[0]
    b=dic[b]
    price=a+b+'元'

elif(lenth==7): #处理000的情况
    # o='<d class=\"num\">&#xf5d6;</d><d class=\"num\">&#xeedb;</d><d class=\"num\">&#xf26a;</d>'
    # ['<d class="num"', '&#xf5d6;</d', '<d class="num"', '&#xeedb;</d', '<d class="num"', '&#xf26a;</d', '']
    a=obj_price.split('>')[1].split(';')[0]
    a=dic[a]
    b=obj_price.split('>')[3].split(';')[0]
    b=dic[b]
    c=obj_price.split('>')[5].split(';')[0]
    c=dic[c]
    price=a+b+c+'元'
else:
    price='--(没有)'
# print(price)
# 评分
obj_sore = obj["fiveScore"]
# 口味
obj_taste_1 = obj["shopRefinedScoreValueList"][0].split('>')[1].split(';')[0]
obj_taste_1=dic[obj_taste_1]
# obj_taste_2 = obj["shopRefinedScoreValueList"][0].split('>')[3].split(';')[0]
obj_taste_2 = obj["shopRefinedScoreValueList"][0].split('>')
if(len(obj_taste_2)==3):
    obj_taste_2 = obj["shopRefinedScoreValueList"][0].split('>')[2]
else:
    obj_taste_2 = obj["shopRefinedScoreValueList"][0].split('>')[3].split(';')[0]
obj_taste_2=dic[obj_taste_2]
obj_taste=obj_taste_1+'.'+obj_taste_2
# 环境
obj_env_1=obj["shopRefinedScoreValueList"][1].split('>')[1].split(';')[0]
obj_env_1=dic[obj_env_1]
# obj_env_2=obj["shopRefinedScoreValueList"][1].split('>')[3].split(';')[0]
# obj_env_2=obj["shopRefinedScoreValueList"][1].split('>')[2]
obj_env_2=obj["shopRefinedScoreValueList"][1].split('>')
if (len(obj_env_2)==3):
    obj_env_2=obj["shopRefinedScoreValueList"][1].split('>')[2]
else:
    obj_env_2=obj["shopRefinedScoreValueList"][1].split('>')[3].split(';')[0]
# print(obj_env_2)

obj_env_2=dic[obj_env_2]
obj_env=obj_env_1+'.'+obj_env_2

# 服务
obj_serve_1=obj["shopRefinedScoreValueList"][2].split('>')[1].split(';')[0]
obj_serve_1=dic[obj_serve_1]
# obj_serve_2=obj["shopRefinedScoreValueList"][2].split('>')[3].split(';')[0]
obj_serve_2=obj["shopRefinedScoreValueList"][2].split('>')
if (len(obj_serve_2)==3):
    obj_serve_2=obj["shopRefinedScoreValueList"][2].split('>')[2]
else:
    obj_serve_2=obj["shopRefinedScoreValueList"][2].split('>')[3].split(';')[0]
# print(obj_serve_2)
obj_serve_2=dic[obj_serve_2]
# print(obj_serve_2)
obj_serve=obj_serve_1+'.'+obj_serve_2

print(obj_sore,price,obj_taste,obj_env,obj_serve)
workbook=xlwt.Workbook()
# 创建一个worksheet
# sheet_name=clib_name
worksheet=workbook.add_sheet('长沙面包甜点汇总')
worksheet.write(0, 0, label='店名')
worksheet.write(0, 1, label='星级')
worksheet.write(0, 2, label='人均')
worksheet.write(0, 3, label='口味')
worksheet.write(0, 4, label='环境')
worksheet.write(0, 5, label='服务')
worksheet.write(0, 6, label='网址查询')
# for i in range(len(src_list)):
i=0
name_list='asdf'
src='http://www.dianping.com/shop/l4hdVw36mOV6n67V'
worksheet.write(i + 1, 0, label=name_list[i])
worksheet.write(i + 1, 1, label=obj_sore)
worksheet.write(i + 1, 2, label=price)
worksheet.write(i + 1, 3, label=obj_taste)
worksheet.write(i + 1, 4, label=obj_env)
worksheet.write(i + 1, 5, label=obj_serve)
worksheet.write(i + 1, 6, label=src)

workbook.save('长沙.xls')

# fp = open('Lbh.xls', 'w', encoding='gbk')
# fp.write(0,0,label='星级')

# fp.write(obj_sore)

# 参数'w'表示往指定表格读入数据，会先将表格中原本的内容清空
# 若把参数’w'修改为‘a+',即可实现在原本内容的基础上，增加新写入的内容


# if(obj[-1]==1):
#     b=str[0]   #处理101的情况
# else:
#     b=str.split('>')[1].split(';')[0]
# # print(b)
# b=str.split('>')[1].split(';')[0]
#
# print(len(str))
# str1='<d class=\"num\">&#xf5d6;</d><d class=\"num\">&#xf5d6;</d>'   #len=5  22yuan
# str1=str1.split('>')
# print(len(str1))
# str2="<d class=\"num\">&#xeedb;</d>1"  #31yuan  len=3
# # str2=str2.split('>')
# print(len(str2))
# str3="1<d class=\"num\">&#xeedb;</d>"  #13yuan  len=3
# # str3=str3.split('>')
# if(str3[0]==1):
#     a=1
# b = str3.split('>')[1].split(';')[0]
# print(b)
# # print(len(str3))
#
# str5='<d class=\"num\">&#xf5d6;</d><d class=\"num\">&#xeedb;</d><d class=\"num\">&#xf26a;</d>'
# c=str5.split('>')
# print(len(c))

# str4='11'  #11yuan  len=0
#
# print(len(str4))


# a=str.split('>')[0].split('<')[0]   # 取到首位1   107元
# b=str[0]
#
# print(b)


# ['1<d class="num"', '&#xeedb;</d', '']  len=3   13yuan
# &#xeedb
#
# 3元
# 3.9