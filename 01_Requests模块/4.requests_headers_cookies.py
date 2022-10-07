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
    "cookie": "_octo=GH1.1.2129475012.1652808667; _device_id=cdc51093b3b7843be25cd2740cc64bc5; has_recent_activity=1; color_mode=%7B%22color_mode%22%3A%22auto%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%7D; preferred_color_mode=light; tz=Asia%2FShanghai; user_session=qcuFyboJEVwS_TiRecNe3vGCtVVkol_tFMQGk2SsL_lSNhnk; __Host-user_session_same_site=qcuFyboJEVwS_TiRecNe3vGCtVVkol_tFMQGk2SsL_lSNhnk; tz=Asia%2FShanghai; logged_in=yes; dotcom_user=yang-12345678; _gh_sess=fRq%2FDiYnOrcI5d2q57QxUciTpO7vZ0UpTB4qQhxOxjHxobpwkTpOnDjktpfo5Nf7D65QNrr1JiZdMqjXr9lU0n%2ByBS%2BYNPklQucjd5FWDQfou4El%2Bd0pW7lDpBu2qGoFfmpV7hcFUd0TFb3fqLnpzMwRy2x5CR%2BcU5KOZWwGOQw%2BVQTrXv4b98lKOHOsdw4To1FUhZdo3pXImE5iTInP01r7O5znp53Ma%2BbzWGGB4dcbJnB32o6wvM0le%2Fj3ssVVcCs8MCv8rrU6NRA3%2BNoJnPi%2FsBZtGArPf6WRfIh8grniQo2xe3f1AcIWNa5%2B%2FrGYvAyhskNksiECn%2FO0FWXcz%2BWnoHn%2BIIg3LXhoc5GaLBdZn4IOl%2BxRKagGZABasO5%2FdEt5AyE47VjNU%2Fgl28zEaULm%2FgsWVeGZQzOB5HnGfodmVqpFJ769yCktrOZ8%2BG8qEhbCYRQbGmZZz6EeTWy5iph%2F2%2Bo6KlAPwXsCI2j%2BEKkaBaCkS0yNOR6R0t4m7pJdUtztyLXsDFlbH6rADI%2B7DphaxfZFsbFvIf64jleqOZjf5%2Bdkgua3q4h4kE5hEMAg9fRPe23F0u6q0JJG9xpi6KDpWmrHg2Y4wDNIX3FkrWFjp5iysk9DuaitT8T6U1tZMI5BXOpZwbSpzOsWQN002dfKiJQsd2frV%2BdZWVIqHZ8byfMKr4rMV9Vvi8qGIoGqak1QD1gHknwQEHz8LT8t5BtgGNKKI79nZ%2FcQYdQIaoRKYfPOUCZEZK979nCJR1eF9L5rt6J7xP8gYrAL7qMfGpWK7xQ%3D--VVWqgBZ33tj%2BL1B0--d17up%2Fj55Fc68BNgB%2BdxOA%3D%3D"
}

response = requests.get(url, headers=headers)

with open("github_with_cookies.html", "wb") as f:
    f.write(response.content)
