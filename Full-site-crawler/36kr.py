from urllib.parse import urljoin
from lxml import etree
import requests
from queue import Queue
from baseClass import Spider
from pymongo import MongoClient

flt = lambda x: x[0] if x else None


class Crawl(Spider):
    base_url = "https://36kr.com/"
    start_url = "https://36kr.com/information/technology"
    # 解析规则
    rules = {
        # 文章列表
        "list_urls": '//div[@class="article-item-pic-wrapper"]/a/@href',
        # 详情页数据
        "detail_urls": '//div[@class="common-width margin-bottom-20"]/text()',
        # 标题
        "title": '//h1[@class="article-title margin-bottom-20 common-width"]/text()',
    }
    # 定义队列
    list_queue = Queue()

    def crawl(self, url):
        # 首页
        response = self.fetch(url)
        list_urls = etree.HTML(response.text).xpath(self.rules["list_urls"])
        for list_url in list_urls:
            self.list_queue.put(urljoin(self.base_url, list_url))

    def list_loop(self):
        # 采集列表页
        while True:
            list_url = self.list_queue.get()
            print(self.list_queue.qsize())
            self.crawl_detail(list_url)
            # 如果队列为空，退出程序
            if self.list_queue.empty():
                break

    def crawl_detail(self, url):
        # 详情页
        response = self.fetch(url)
        html = etree.HTML(response.text)
        content = html.xpath(self.rules["detail_urls"])
        title = flt(html.xpath(self.rules["title"]))
        print(title)
        data = {"content": content, "title": title}
        self.save_mongo(data)

    def save_mongo(self, data):
        client = MongoClient()
        col = client["python"]["hh"]
        if isinstance(data, dict):
            res = col.insert_one(data)
            return res
        else:
            return f'单条数据必须是{"name":"age"}格式，你传入的格式是{type(data)}'

    def main(self):
        self.crawl(self.start_url)
        self.list_loop()


if __name__ == "__main__":
    s = Crawl()
    s.main()
