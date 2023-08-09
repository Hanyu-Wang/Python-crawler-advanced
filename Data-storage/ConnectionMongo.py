import os
import httpx
import pymongo


mongo_con = os.getenv('MONGO_CONNECTION')
client = pymongo.MongoClient(mongo_con)
"""
pymongo升级到4.0后的认证方式更改 https://pymongo.readthedocs.io/en/stable/migrate-to-pymongo4.html#database-authenticate-and-database-logout-are-removed
"""
db = client.whytest
collection = db["students"]


def get_data():
    res = httpx.get(
        "https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1691550385360&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=%25E6%25B5%258B%25E8%25AF%2595&pageIndex=1&pageSize=10&language=zh-cn&area=cn"
    )
    items = res.json()
    item = items.get("Data")["Posts"]
    for i in item[0:1]:
        if isinstance(i, dict):
            collection.insert_one(i)


if __name__ == "__main__":
    get_data()
