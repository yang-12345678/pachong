"""作用：
可以利用cookies跟踪统计用户访问该网站的习惯，比如什么时间访问，访问了哪些页面，在每个网页的停留时间等。
利用这些信息，一方面是可以为用户提供个性化的服务，
另一方面，也可以作为了解所有用户行为的工具，对于网站经营策略的改进有一定参考价值。
可以记录登录信息"""

import requests

url = "https://github.com/yang-12345678"

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
    "cookie": "_octo=GH1.1.2039940894.1646452114; _device_id=32a3a2ed826c041a1ef7f0bcd42755ef; "
              "user_session=NzzFb2SBM5Sik0BT1FENsk6Txx-uSYPw5PId8HqKkts68LIG;"
              " __Host-user_session_same_site=NzzFb2SBM5Sik0BT1FENsk6Txx-uSYPw5PId8HqKkts68LIG; "
              "logged_in=yes; dotcom_user=yang-12345678; has_recent_activity=1; "
              "color_mode=%7B%22color_mode%22%3A%22auto%22%2C%22light_theme%"
              "22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2"
              "C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%2"
              "2%7D%7D; tz=Asia%2FShanghai; _gh_sess=wIwjAbN8nHEmiug9K4JahhV%2FF8E38fcLm%2F3hv6T"
              "q19HNUKyiCnE2%2B4byQAPU5PECWPtEf9Xoar3aI%2F98dnM1JMhnALBb8%2B9VrZXlLqjnpsp1u4KFq2T"
              "ehFfAHShKQ%2FUEhR%2BRRBqensHA6FFwFjXZEss2vmKKLBEjKY6Y7hrCIPDNQzOcqoe1bCF6STUlcHaI-"
              "-KQQRervKbceTTGmQ--mbhkwGFjnmeDlh7U8rIuJw%3D%3D"
}

response = requests.get(url, headers=headers)

with open("github_with_cookies.html", "wb") as f:
    f.write(response.content)

