# -*- coding: gbk -*-
import requests
import chardet
import json
from city import city

# get all cities name
# print(city.keys())
# cities = [i for i in city.keys()]
# for i in cities:
#     print(i)

cityname = input('������ĸ����е�������\n')
citycode = city.get(cityname)
# print(citycode)
if citycode:
   url = ('http://www.weather.com.cn/data/cityinfo/%s.html' % citycode)
   content = requests.get(url).text
   data = json.loads(content)
   # print(type(content)) # string
   # print(type(data)) # dict
else:
   print('û���ҵ��ó���')
try:
    result = data['weatherinfo']
    str_temp = ('%s\n%s ~ %s') % (
        result['weather'],
        result['temp1'],
        result['temp2']
    )
    print(str_temp)
except:
   print('��ѯʧ��')