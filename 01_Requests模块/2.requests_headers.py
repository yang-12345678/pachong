import requests

url = "http://www.baidu.com"

# 发送 get 请求， 获得响应体
response = requests.get(url)

print(len(response.content.decode()))

print(response.request.headers)

# headers参数接收字典形式的请求头
# 请求头字段名作为key，字段对应的值作为value
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/100.0.4896.127 Safari/537.36"
}

# 发送带请求头的请求
response = requests.get(url, headers=headers)

print(len(response.content.decode()))

print(response.request.headers)