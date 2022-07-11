import json
import jsonpath
#  073爬虫_解析_jsonpath.json
obj=json.load(open('cid.json','r',encoding='utf-8'))
# author_list=jsonpath.jsonpath(obj,'$..author')
# author_list=jsonpath.jsonpath(obj,'$.cid.*')
# print(author_list)
# print(obj)
a=obj["SDQOutputSet"][0]["rows"][0]["cid"]
print(a)
# print('cid',':','cid' in obj,':',obj.get('cid'))
# print(obj)