import requests
import json

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
# 人均
# len= obj["avgPrice"].split('>')
# print(a)
def get_price(len):
    if(len==5):
        obj_avgPrice_1 = obj["avgPrice"].split('>')[1].split(';')[0]
        print(obj_avgPrice_1)
        # print(obj_avgPrice_1)
        obj_avgPrice_1=dic[obj_avgPrice_1]
        # print(obj["avgPrice"].split())
        # obj_avgPrice_2 = str(obj["avgPrice"].split('>')[3].split(';')[0])
        obj_avgPrice_2 = obj["avgPrice"].split('>')
        if(len(obj_avgPrice_2)<=3):
            obj_avgPrice_2 = obj["avgPrice"].split('>')[2]
        else:
            # obj_avgPrice_2 = obj["avgPrice"].split('>')[3].split(';')[0]
            obj_avgPrice_2 = obj["avgPrice"].split('>')[3].split(';')[0]
        # obj_avgPrice_2=dic[obj_avgPrice_2]
        print(obj_avgPrice_2)
        obj_avgPrice = obj_avgPrice_1 + obj_avgPrice_2 + '元'
        print(obj_avgPrice)
        return obj_avgPrice
    elif(len==4):
        obj_avgPrice_1 = obj["avgPrice"].split('>')[1].split(';')[0]
        print(obj_avgPrice_1)
        # print(obj_avgPrice_1)
        obj_avgPrice_1=dic[obj_avgPrice_1]
        # print(obj["avgPrice"].split())
        # obj_avgPrice_2 = str(obj["avgPrice"].split('>')[3].split(';')[0])
        obj_avgPrice_2 = obj["avgPrice"].split('>')
        if(len(obj_avgPrice_2)<=3):
            obj_avgPrice_2 = obj["avgPrice"].split('>')[2]
        else:
            # obj_avgPrice_2 = obj["avgPrice"].split('>')[3].split(';')[0]
            obj_avgPrice_2 = obj["avgPrice"].split('>')[3].split(';')[0]
        # obj_avgPrice_2=dic[obj_avgPrice_2]
        print(obj_avgPrice_2)
        obj_avgPrice = obj_avgPrice_1 + obj_avgPrice_2 + '元'
        print(obj_avgPrice)
        return obj_avgPrice
    else:
        pass

if(len(obj["avgPrice"])>2): #考虑价格11元
    len= len(obj["avgPrice"].split('>'))
    obj_avgPrice=get_price(len)
else:
    obj_avgPrice='11'


# 评分
obj_sore = obj["fiveScore"]
# 口味
obj_taste_1 = obj["shopRefinedScoreValueList"][0].split('>')[1].split(';')[0]
obj_taste_1=dic[obj_taste_1]
# obj_taste_2 = obj["shopRefinedScoreValueList"][0].split('>')[3].split(';')[0]
obj_taste_2 = obj["shopRefinedScoreValueList"][0].split('>')
if(len(obj_taste_2)<=3):
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
if (len(obj_env_2)<=3):
    obj_env_2=obj["shopRefinedScoreValueList"][1].split('>')[2]
else:
    obj_env_2=obj["shopRefinedScoreValueList"][1].split('>')[3].split(';')[0]
# print(obj_env_2)

obj_env_2=dic[obj_env_2]
obj_env=obj_env_1+'.'+obj_env_2
print(obj_env)

# 服务
obj_serve_1=obj["shopRefinedScoreValueList"][2].split('>')[1].split(';')[0]
obj_serve_1=dic[obj_serve_1]
# obj_serve_2=obj["shopRefinedScoreValueList"][2].split('>')[3].split(';')[0]
obj_serve_2=obj["shopRefinedScoreValueList"][2].split('>')
if (len(obj_serve_2)<=3):
    obj_serve_2=obj["shopRefinedScoreValueList"][2].split('>')[2]
else:
    obj_serve_2=obj["shopRefinedScoreValueList"][2].split('>')[3].split(';')[0]
# print(obj_serve_2)
obj_serve_2=dic[obj_serve_2]
# print(obj_serve_2)
obj_serve=obj_serve_1+'.'+obj_serve_2

# print(obj_avgPrice, obj_sore, obj_taste,obj_env,obj_serve)

# request=urllib.request.Request(url=url,headers=headers)
# response=urllib.request.urlopen(request)
# # content=response.read().decode('utf-8')
# content=response.text
# tree=etree.HTML(content)
# name=tree.xpath('//div')
# print(name)
