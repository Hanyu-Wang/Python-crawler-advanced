from pymongo import MongoClient
from pyhocon import ConfigFactory

conf = ConfigFactory.parse_file("database.conf")
host = conf.get("database.mongo.host")
port = conf.get("database.mongo.port")
username = conf["databases"]["mongo"]["username"]
password = conf.get_config("databases")["mongo.password"]
client = MongoClient(host, port)
db_auth = client.whytest
db_auth.authenticate(username, password)
