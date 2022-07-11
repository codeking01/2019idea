import json
import openpyxl
import random
import requests
import urllib.request
import pymysql

# 打开数据库连接
db = pymysql.connect(host="localhost", user="root", password="123456", database="pubimage")
# 使用cursor（）方法获取游标
cursor = db.cursor()

if __name__ == '__main__':
    # excel中的数据的 A1 取出来有个引号 从A2开始取数据
    # r = 2
    # query_list = ['115754-20-6']
    # index用来计数
    index = 0
    # 需要定制的请求头
    headers = {
        'referer': 'https://pubchem.ncbi.nlm.nih.gov/'
    }
    # 加代理池
    proxies_pool = [
        {'http': '112.195.241.83: 3256'},
        {'http': '117.94.222.222: 3256'},
        {'http': '117.94.222.28	: 3256'},
        {'http': '121.230.211.227:3256'},
        {'http': '111.72.25.79:3256'},
        {'http': '47.75.132.50:8118'},
        {'http': '27.191.60.200:3256'},
        {'http': '219.151.142.29:3128'},
        {'http': '211.65.197.93:80'},
        {'http': '211.65.197.93:80'},
        {'http': '121.232.148.242:3256'},
    ]
    # 处理失败的数据
    cursor.execute("select cas,src from failedlist")
    # 查看表里所有数据
    data = list(cursor.fetchall())

    for i in data:
        index+=1
        try:
            cas = i[0].replace('_', '-')
            url = 'https://pubchem.ncbi.nlm.nih.gov/sdq/sdqagent.cgi?infmt=json&outfmt=json&query={%22select%22:%22*%22,%22collection%22:%22compound%22,%22where%22:{%22ands%22:[{%22cid%22:%22' + str(
                cas) + '%22}]},%22order%22:[%22cid,asc%22],%22start%22:1,%22limit%22:10,%22width%22:1000000,%22listids%22:0}'
            proxies = random.choice(proxies_pool)
            response = requests.get(url=url, headers=headers, proxies=proxies)
            response.encoding = 'utf-8'
            # 下面这个json数据可以采集到
            json_content = response.text
            # print(page_content)
            # ***可以直接读取json，就不存进去了
            obj = json.loads(json_content)
            # 找到json中相应的数据
            obj_cid = obj["SDQOutputSet"][0]["rows"][0]["cid"]
            # print(obj_cid)    这个地方是根据cid号进行下载的，做了加密，直接解析是获取不到地址的

            down_src = 'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/CID/' + str(
                obj_cid) + '/record/SDF/?record_type=3d&response_type=save&response_basename=Conformer3D_CID_' + str(
                obj_cid)
            urllib.request.urlretrieve(down_src, './3D_pic/Conformer3D_CID_' + str(cas) + '.sdf')
            insert_sql = "insert into test(cas,image, src) values(%s,%s,%s)"
            fp = open("./3D_pic/Conformer3D_CID_" + str(cas) + '.sdf', 'rb')
            img = fp.read()
            fp.close()
            parm = (cas, img, down_src)
            cursor.execute(insert_sql, parm)
            db.commit()
            print('第{0}条数据下载成功'.format(index))
        except:
            cas_new = cas.replace('-', '_')
            insert_sql = "insert into failedlist_sec(cas, src,cas_new) values(%s, %s,%s)"
            parm = (cas, down_src,cas_new)
            cursor.execute(insert_sql, parm)
            db.commit()
            print('Waring：第{0}条数据下载失败.....正在记录，请稍后...'.format(index))
