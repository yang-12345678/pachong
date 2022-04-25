import requests

url = "http://www.baidu.com"

# 如果代理使用成功，不会有任何报错，能成功获取响应
# 如果失败，要么卡滞，要么报错

proxies = {
    "http": "64.227.62.123:80",
    # "https": "https://218.95.81.51:9000"
}

# response = requests.get(url)
response = requests.get(url, proxies=proxies)

print(response.text)