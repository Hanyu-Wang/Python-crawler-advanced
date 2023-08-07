from urllib.parse import urljoin
import requests
from queue import Queue
from baseClass import Spider
from pymongo import MongoClient

flt = lambda x: x[0] if x else None


class Crawl(Spider):
    pass
