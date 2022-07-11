from lxml import etree
# 1.解析本地文件
# 2.解析服务器响应的数据
#  for_xpath_applicate.html

# etree.parse() 解析 本地文件
# etree.HTML() 解析服务器响应件
tree=etree.parse('for_xpath_applicate.html')
# print(tree)
# 下面是 xapth的语法结构 text()获取标签中的内容的
# ul_list=tree.xpath('//body/ul/li[@id]/text()')
ul_list=tree.xpath('//body')
print(ul_list)
print(len(ul_list))

