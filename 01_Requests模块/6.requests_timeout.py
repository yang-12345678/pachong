import requests

url = "https://twitter.com"

# 在爬虫中，一个请求很久没有结果，就会让整个项目的效率变得非常低，这个时候我们就需要对请求进行强制要求，让他必须在特定的时间内返回结果，否则就报错。

# timeout=3表示：发送请求后，3秒钟内返回响应，否则就抛出异常
response = requests.get(url, timeout=3)