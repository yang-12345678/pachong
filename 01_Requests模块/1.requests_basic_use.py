import requests

url = "http://www.baidu.com"

# 发送 get 请求， 获得响应体
response = requests.get(url)


"""
# 解决乱码方式1

# 查看源码编码方式
# print(response.encoding)

# 改变了response的编码格式
# response.encoding = 'utf-8'

# response.text 存储的是 str 类型的数据
# response.text 相当于 response.content.decode('推测出的编码字符集')   可能有乱码
# print(response.text)

# print(response.encoding)"""

"""
# 解决乱码方式2

# respons.content 存储的是 bytes 类型的响应数据， 可以进行 decoding 操作
print(response.content.decode())  # decode() 默认使用 utf8 解码"""

# 常见的响应对象参数和方法
# 相应url
print(response.url)

# 状态码
print(response.status_code)

# 打印响应对象请求头
print(response.headers)

# 打印响应对象对应请求的请求头
print(response.request.headers)
