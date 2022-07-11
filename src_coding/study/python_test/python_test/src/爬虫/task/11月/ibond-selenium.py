#开发时间：2021/10/22   16:57
#coding:utf-8

import random
import os
import requests
import json
import time
import xlwt
import xlsxwriter
from time import sleep
from selenium import webdriver
from fake_useragent import UserAgent



# selenium获取cookie
bro=webdriver.Firefox(executable_path='./geckodriver.exe')
bro.get('http://ibond.nankai.edu.cn/accounts/login/?next=/pka/')
time.sleep(10)


#定位到账号标签
userName_tag=bro.find_element_by_xpath('//*[@id="id_username"]')
#定位密码标签
pass_tag=bro.find_element_by_xpath('//*[@id="id_password"]')
#录入用户名
userName_tag.send_keys('Fengxiaojie')
#录入用户密码
sleep(1)
pass_tag.send_keys('fxjie1998')
#定位登录按钮
btn=bro.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/form/fieldset/div[3]/input')
#点击登录按钮
btn.click()
sleep(3)

csrfmiddlewaretoken=input('请输入csrfmiddlewaretoken:')
sleep(3)



clib_list=[
    # {'selected_node': 'Monoacids', 'page':69},
    # {'selected_node': 'Polyacids', 'page':56},
    # {'selected_node': 'Monacids', 'page': 4},
    # {'selected_node': 'Benzoic acids', 'page': 118},
    # {'selected_node': 'Phenylacetic acids and derivatives', 'page': 72},
    # {'selected_node': 'Anilines', 'page': 129},
    # {'selected_node': 'Aromatic rings on side chain', 'page': 35},
    # {'selected_node': 'Primary amines', 'page': 15},
    # {'selected_node': 'Secondary amines', 'page': 10},
    # {'selected_node': 'Tertiary amines', 'page': 14},
    # {'selected_node': 'Quaternary amines', 'page': 2},
    # {'selected_node': 'Polyamines', 'page': 18},
    # {'selected_node': 'Non-aromatic cyclic amines', 'page': 55},
    # {'selected_node': 'Hydroxylamines and hydrazines', 'page': 63},
    # {'selected_node': 'Pyridines', 'page': 47},
    # {'selected_node': 'Pyridine-N-oxides', 'page': 11},
    {'selected_node': 'Imidazoles, thiazoles and triazoles', 'page': 102},
    # {'selected_node': 'Pyrimidines, pyridazines and pyrazines', 'page': 71},
    # {'selected_node': 'Imidazoles, thiazoles and Triazoles', 'page': 36},
    # {'selected_node': 'Quinolines', 'page': 42},
    # {'selected_node': 'Cinnolines, phthalazines, quinoxalines and quinazolines', 'page': 64},
    # {'selected_node': 'Benziminazoles and indazoles', 'page': 51},
    # {'selected_node': 'Polycyclic compounds', 'page': 43},
    # {'selected_node': 'C=O', 'page': 63},
    # {'selected_node': 'CONH2', 'page': 42},
    # {'selected_node': 'CO2R', 'page': 19},
    # {'selected_node': 'Ureas', 'page': 21},
    # {'selected_node': 'CN', 'page': 21},
    # {'selected_node': 'NO2 and NO', 'page': 23},
    # {'selected_node': 'C=N', 'page': 13},
    # {'selected_node': 'Amidines and guanidines', 'page': 45},
    # {'selected_node': 'S', 'page': 23},
    # {'selected_node': 'SO', 'page': 6},
    # {'selected_node': 'SO2', 'page': 97},
    # {'selected_node': 'Organic phosphoric acids', 'page': 50},
    # {'selected_node': 'Organic phosphoric compounds', 'page': 25},
    # {'selected_node': 'Neutral amino acids', 'page': 38},
    # {'selected_node': 'Acidic amino acids', 'page': 12},
    # {'selected_node': 'Peptides', 'page': 19},
    # {'selected_node': 'Alkaloids', 'page': 207},
    # {'selected_node': 'Non-aromatic heterocyclic compounds', 'page': 21},
    # {'selected_node': 'Metallic compounds', 'page': 26},
    # {'selected_node': 'Phenols', 'page': 155},
    # {'selected_node': 'Alcohols', 'page': 66},
    # {'selected_node': 'Ethers and peroxides', 'page': 10},
    # {'selected_node': 'Hydroxamic acids', 'page': 26},
    # {'selected_node': 'Oximes', 'page': 30},
]

for c in range(len(clib_list)):
    #创建要下载的文件夹
    # 文件夹 后面需将图片存入
    clib_name=clib_list[c]['selected_node']       #   要改
    clib='./'+clib_name
    if not os.path.exists(clib):
        os.mkdir(clib)

    # 创建一个workbook，设置编码
    book_name='ibond数据_'+clib_name
    workbook=xlwt.Workbook()
    # 创建一个worksheet
    # sheet_name=clib_name
    worksheet=workbook.add_sheet('sheet1')
    # 写入Excel
    # 参数对应 行，列，值
    # 首行内容写入
    worksheet.write(0, 0, label='mol_id')
    worksheet.write(0, 1, label='ref_doi')
    worksheet.write(0, 2, label='ref_content')
    worksheet.write(0, 3, label='solvent__full_name')
    worksheet.write(0, 4, label='solvent__name')
    worksheet.write(0, 5, label='method__description')
    worksheet.write(0, 6, label='pKa')
    worksheet.write(0, 7, label='method__name')
    worksheet.write(0, 8, label='ref__ref_no')
    worksheet.write(0, 9, label='img')
    worksheet.write(0, 10, label='img_url')
    worksheet.write(0, 11, label='mol_name')

    all_list=[]
    page=clib_list[c]['page']
    for i in range(1,page):       #   改range
        inorganic_acids=bro.find_element_by_xpath('//*[@id="j1_1_anchor"]')
        inorganic_acids.click()
        sleep(3)
        cook=bro.get_cookies()
        # print(cook)
        FSSBBIl1UgzbN7N80S=cook[0]["value"]
        sessionid=cook[1]["value"]
        csrftoken=cook[2]["value"]
        FSSBBIl1UgzbN7N80T=cook[3]["value"]
        cook='FSSBBIl1UgzbN7N80S='+FSSBBIl1UgzbN7N80S+';'+'sessionid='+sessionid+';'+'csrftoken='+csrftoken+';'+'FSSBBIl1UgzbN7N80T='+FSSBBIl1UgzbN7N80T
        # print(cook)

        headers = {
            'Accept': '*/*',
            'Connection': 'keep-alive',
            'Cookie': cook,
            # 'Host': 'ibond.nankai.edu.cn',
            # 'Origin': 'http://ibond.nankai.edu.cn',
            # 'Referer': 'http://ibond.nankai.edu.cn/pka/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
        }
        selected_node=clib_list[c]['selected_node']
        data={
                'input_filter_type': 'pka',
                # 'keyword': 'ammonia',
                'selected_node': selected_node,        #   变动的
                'similarity_type': 'similarity',
                'solvent_select': 'All',
                'csrfmiddlewaretoken': csrfmiddlewaretoken,          # 变动的
                'input_keyword_type': 'name',
                'page_num': str(i)
            }
        post_url = 'http://ibond.nankai.edu.cn/pka/search/?'
        response = requests.post(url=post_url, data=data, headers=headers)
        print(response)
        page_text = response.text
        # print(page_text)
        jsonobj = json.loads(page_text)  # 将响应内容转换为Json对象
        # 取json内容
        for b in range(len(jsonobj["dis_point_list"])):
            for a in range(len(jsonobj["dis_point_list"][b]["dissociation_set"])):
                # b指每页的结构总数
                mol_id = jsonobj["dis_point_list"][b]["mol_id"]
                # a指同一结构下测试pka的方法数
                ref_doi=jsonobj["dis_point_list"][b]["dissociation_set"][a]["ref__doi"]
                ref_content=jsonobj["dis_point_list"][b]["dissociation_set"][a]["ref__ref_content"]
                solvent__full_name=jsonobj["dis_point_list"][b]["dissociation_set"][a]["solvent__full_name"]
                solvent__name=jsonobj["dis_point_list"][b]["dissociation_set"][a]["solvent__name"]
                method__description=jsonobj["dis_point_list"][b]["dissociation_set"][a]["method__description"]
                pKa=jsonobj["dis_point_list"][b]["dissociation_set"][a]["pKa"]
                method__name=jsonobj["dis_point_list"][b]["dissociation_set"][a]["method__name"]
                ref__ref_no=jsonobj["dis_point_list"][b]["dissociation_set"][a]["ref__ref_no"]
                img=jsonobj["dis_point_list"][b]["img"]
                img_url='http://ibond.nankai.edu.cn/static/media/'+img
                mol_name=jsonobj["dis_point_list"][b]["mol_name"]
                dic={
                    'mol_id':mol_id,
                    'ref_doi':ref_doi,
                    'ref_content':ref_content,
                    'solvent__full_name':solvent__full_name,
                    'solvent__name':solvent__name,
                    'method__description':method__description,
                    'pKa':pKa,
                    'method__name':method__name,
                    'ref__ref_no':ref__ref_no,
                    'img':img,
                    'img_url':img_url,
                    'mol_name':mol_name
                }
                all_list.append(dic)



    # 写入sheet表
    for i in range(len(all_list)):
        worksheet.write(i + 1, 0, label=all_list[i]['mol_id'])
        worksheet.write(i + 1, 1, label=all_list[i]['ref_doi'])
        worksheet.write(i + 1, 2, label=all_list[i]['ref_content'])
        worksheet.write(i + 1, 3, label=all_list[i]['solvent__full_name'])
        worksheet.write(i + 1, 4, label=all_list[i]['solvent__name'])
        worksheet.write(i + 1, 5, label=all_list[i]['method__description'])
        worksheet.write(i + 1, 6, label=all_list[i]['pKa'])
        worksheet.write(i + 1, 7, label=all_list[i]['method__name'])
        worksheet.write(i + 1, 8, label=all_list[i]['ref__ref_no'])
        worksheet.write(i + 1, 9, label=all_list[i]['img'])
        worksheet.write(i + 1, 10, label=all_list[i]['img_url'])
        worksheet.write(i + 1, 11, label=all_list[i]['mol_name'])
        workbook.save(book_name + '.xls')           # 保存
        print('第'+str(i)+'条获取成功！')
    print('获取结束！')
bro.quit()









