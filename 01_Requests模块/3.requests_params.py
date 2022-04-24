import requests

# 1、在 url 中直接添加参数
# url = "https://www.baidu.com/s?wd=python"
#
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
#                   "Chrome/100.0.4896.127 Safari/537.36",
#     "Accept": "text/html,application/xhtml+xml,application/xml;" \
#               "q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
# }
#
# # 发送 get 请求， 获得响应体
# response = requests.get(url, headers=headers)
# with open("baidu.html", "wb") as f:
#     f.write(response.content)

url = "https://www.baidu.com/s?"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/100.0.4896.127 Safari/537.36",
    # "Accept": "text/html,application/xhtml+xml,application/xml;" \
    #           "q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
}

# 构建参数字典
data = {
    'wd': 'python'
}

# 发送 get 请求， 获得响应体
response = requests.get(url, headers=headers, params=data)

print(response.url)
with open("baidu1.html", "wb") as f:
    f.write(response.content)
