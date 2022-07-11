# -*- codeing =utf-8 -*-
# @Time : 2022/1/11 12:53
# @Author : Hexy
# @File : ACS.py
# @Software: PyCharm
import requests
from bs4 import BeautifulSoup
import parser
import xlwt
import urllib.request, urllib.error
import re

head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"
}


def main():

    baseurl = "https://pubs.acs.org/action/doSearch?AllField=qsar&pageSize=20&startPage="
    datalist = getData(baseurl)

    savepath = ".\\qsar(1).xls"
    saveDate(datalist, savepath)


# findtitle=re.compile(r'<h2 class="issue-item_title"><a href="/doi/(.*?)">(^[\u4e00-\u9fa5\w\.。\' \" ]+$)<span onclick="highlight()" class="single_highlight_class">QSAR</span> (^[\u4e00-\u9fa5\w\.。\' \" ]+$)</a></h2>')
#
#findtitle = re.compile(r'''< a href=" ">(.*?)<span onclick="highlight.* class="single_highlight_class">(.*?)</span>(.*?)</.*''')

findautor=re.compile(r'<span class="hlFld-ContribAuthor">(.*?)</span>')
findoi=re.compile(r'<span class="issue-item_doi"><span>DOI: </span>(.*?)</span>')


def getData(baseurl):
    datalist = []
    for i in range(0, 1):
        url = baseurl + str(i * 20)
        # html = askURL(url)
        response = requests.get(url, headers=head)
        # soup = BeautifulSoup(html, "lxml")
        soup = BeautifulSoup(response.text, 'lxml')
        # print(html)

        #print(soup)

        for item in soup.find_all('div', class_="issue-item clearfix"):
            #print(item)
            data = []
            item = str(item)
            #title = re.findall(findtitle, item)

            #data.append(title)
            author=re.findall(findautor,item)
            data.append(author)

            doi = re.findall(findoi, item)
            data.append(doi)
            datalist.append(data)

            #print(datalist)
            return datalist


def askURL(url):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"
    }
    request = urllib.request.Request(url=url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):  # hasattr函数用于判断对象是否包含相应的属性  hasattr(object对象,name字符串)
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


def saveDate(datalist,savepath):
    book = xlwt.Workbook(encoding="utf-8",style_compression=0)
    sheet = book.add_sheet('qsar(1)',cell_overwrite_ok=True)
    col=("作者","DOI")
    for i in range(0,len(col)):
        sheet.write(0,i,col[i])
    for i in range(0,20):
        print("第%d条"%(i+1))
        date=datalist[i]
        for j in range(0,len(col)):
            sheet.write(i+1,j,date[j])
    book.save(savepath)


if __name__ == '__main__':  # 调用main
    main()

print("爬取成功！")
