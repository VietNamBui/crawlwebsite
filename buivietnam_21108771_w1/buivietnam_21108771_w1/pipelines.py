# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import redis
from scrapy.exceptions import DropItem

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem

# class Buivietnam21108771W1Pipeline:
#     def process_item(self, item, spider):
#         return item

class MongoDBPipeline:
    def __init__(self):
        self.client = pymongo.MongoClient('mongodb://mongo_db:27017/')  
        self.db = self.client['BookstoreDB']
        self.collection = self.db['books']

        # Kết nối Redis
        self.redis_client = redis.Redis(host='redis_db', port=6379, decode_responses=True)

    def process_item(self, item, spider):
        try:
            # Kiểm tra trùng lặp bằng Redis
            if self.redis_client.sismember("scrapy:book_urls", item['tensach']):
                raise DropItem("Duplicate book found: %s" % item['tensach'])
            
            # Lưu vào MongoDB
            self.collection.insert_one(dict(item))

            # Thêm vào danh sách đã crawl trong Redis
            self.redis_client.sadd("scrapy:book_urls", item['tensach'])
            
            print("Cào thành công!!!")
            return item
        except Exception as e:
            raise DropItem(f"Error inserting item: {e}")

    def close_spider(self, spider):
        self.client.close()