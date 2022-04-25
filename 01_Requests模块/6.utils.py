import requests

url = "http://www.baidu.com"

response = requests.get(url)
# 该属性值是一个cookieJar类型，包含了对方服务器设置在本地的cookie
print(response.cookies)

dict_cookies = requests.utils.dict_from_cookiejar(response.cookies)
print(dict_cookies)

dict_cookies = requests.utils.cookiejar_from_dict(dict_cookies)
print(dict_cookies)