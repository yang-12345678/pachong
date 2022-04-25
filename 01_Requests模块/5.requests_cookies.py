import requests

url = "https://github.com/yang-12345678"

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",

}

# 构建cookies字典
temp = "_octo=GH1.1.2039940894.1646452114; _device_id=32a3a2ed826c041a1ef7f0bcd42755ef; user_session=NzzFb2SBM5Sik0BT1FENsk6Txx-uSYPw5PId8HqKkts68LIG; __Host-user_session_same_site=NzzFb2SBM5Sik0BT1FENsk6Txx-uSYPw5PId8HqKkts68LIG; logged_in=yes; dotcom_user=yang-12345678; has_recent_activity=1; color_mode=%7B%22color_mode%22%3A%22auto%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%7D; tz=Asia%2FShanghai; _gh_sess=aPS2I58Q2G3uTjRg05Jh%2FN3Lsf%2B25coKxNULac4OYpvEo48ZCzCEFrK8rxd860D2ZLaqnOkD8bXmfzbLXoYOsqgtzyRzTd36%2BzSNVYWXyVtJTBx5NPDLigA8M9Jz9yUknkjLTcvnSbf4Kz9WmbKKL6HmYJczb2mP0PlYtVOXN7ZgLZQ70q88RjV9MABqM0cM--zRIK0EMYfAb3TEu0--2%2FXdLeDq9UstfnuNukMTZQ%3D%3D"

cookie_list = temp.split("; ")
# 稳妥方案

# print(cookie_list)
# cookies = {}
# for cookie in cookie_list:
#     cookies[cookie.split("=")[0]] = cookie.split("=")[-1]
# print(cookies)

# 字典推导式
cookies = {cookie.split("=")[0]: cookie.split("=")[1] for cookie in cookie_list}

response = requests.get(url, headers=headers, cookies=cookies)

with open("github_with_cookies3.html", "wb") as f:
    f.write(response.content)
