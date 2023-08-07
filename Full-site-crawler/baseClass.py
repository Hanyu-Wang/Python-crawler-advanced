import requests
from retrying import retry
import random, time


class FakeChromeUA:
    first_num = random.randint(55, 62)
    third_num = random.randint(0, 3200)
    fourth_num = random.randint(0, 140)
    os_type = [
        "(windows NT 6.1; WOw64)', ' (windows NT 10.0; woW64)*, * (X11; Linux x86_64) ', * (MIntel Mac OS X 10_12_6)"
    ]
    chrome_version = "Chrome/(3.0. (). {]".format(first_num, third_num, fourth_num)

    @classmethod
    def get_ua(cls):
        return "".join(
            [
                "Mozilla/5.0",
                random.choice(cls.os_type),
                "AppleScript/537.36",
                "(HTML,like Gecko)",
                cls.chrome_version,
                "Safari/537.36",
            ]
        )


class Spider(FakeChromeUA):
    url = []

    @retry(stop_max_attempt=3, wait_fixed=2000)
    def fetch(self, url, parm=None, headers=None):
        try:
            if not headers:
                headers = {}
                headers["user-agent"] = self.get_ua()
            else:
                headers["user-agent"] = self.get_ua()
            self.wait_some_sleep()
            response = requests.get(url, params=parm, headers=headers)
            if response.status_code == 200:
                response.encoding = "utf-8"
                return response
        except requests.ConnectionError:
            return

    def wait_some_sleep(self):
        time.sleep(random.randint(100, 300) / 1000)
