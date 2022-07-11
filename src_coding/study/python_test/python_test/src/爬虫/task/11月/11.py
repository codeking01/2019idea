import requests

url = 'http://www.dianping.com/ajax/json/shopDynamic/reviewAndStar?shopId=l6c49QrTQEWGFItd&cityId=344&mainCategoryId=34237'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
    'Cookie': 'navCtgScroll=0; _lxsdk_cuid=17c7f907122c8-005a3d1714b78c-b7a1438-144000-17c7f907122c8; _lxsdk=17c7f907122c8-005a3d1714b78c-b7a1438-144000-17c7f907122c8; _hc.v=751dd7ad-f61c-e41b-0401-95d1866ae493.1634227745; s_ViewType=10; ua=dpuser_15059620632; ctu=1dc952f673738fa47d20413160405840235920484dc849760c4a66b318dd0f6b; fspop=test; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1634227745,1635433785,1635434475; cy=344; cye=changsha; thirdtoken=41702c09-7086-430b-ab15-e7448c57e6c0; dper=234cb94f92704aef13a7e6c816ada0ec5d82dfce20785f8f7461236e5ad4452e080a2eb9d7089f0779c7dccdb93f453054a0e3dd272f57e46cf3f29951cb4adf5159c53995424956e2bae8b3aa6d15febd25ed5e382eabe35e43e4007f6a7b94; ll=7fd06e815b796be3df069dec7836c3df; ctu=b58a9fce079b27059480a633b27a83c81b97ef52648306836b7b2a7e61a47c0127548a04b35974cf992382a35b6cbb17; dplet=7a0ee364bff4bc2bf9ed9183621d7340; _lxsdk_s=17cc773261d-562-249-600%7C%7C710; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1635436153'
}
response=requests.get(url=url,headers=headers)
print(response.text)