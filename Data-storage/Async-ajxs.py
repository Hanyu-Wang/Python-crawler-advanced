# encoding:utf-8

import requests


def get_data():
    url = "https://danjuanfunds.com/djapi/fund/growth/002180?day=1m"
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/89.0.4389.114 Safari/537.36",
    }
    res = requests.get(url, headers=headers).json()
    print(res)


get_data()
