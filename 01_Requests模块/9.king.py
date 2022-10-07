import requests
import json


class King:
    def __init__(self, word):
        self.url = "http://ifanyi.iciba.com/index.php?c=trans&m=fy&client=6&auth_user=key_ciba&sign=f4be9753e84bcbf0"

        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
        }

        self.data = {
            "from": "zh",
            "to": "en",
            "q": word
        }

    def get_data(self):
        # 使用post方法发送一个post请求，data为请求体的字典
        response = requests.post(self.url, data=self.data, headers=self.headers)
        return response.content

    def parse_data(self, data):
        # loads方法将json字符串转换成python字典
        dict_data = json.loads(data)
        print(dict_data['content']['out'])

    def run(self):
        # 编写爬虫逻辑
        # url
        # headers
        # data字典
        # 发送请求，获取响应
        response = self.get_data()
        print(response)
        # 数据解析
        self.parse_data(response)


if __name__ == '__main__':
    king = King("1")
    king.run()
