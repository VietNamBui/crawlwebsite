# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import json
import csv
import mysql.connector
import psycopg2

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem

# class Buivietnam21108771W1Pipeline:
#     def process_item(self, item, spider):
#         return item

# class MongoDBPipeline:
#     def __init__(self):
#         self.client = pymongo.MongoClient('mongodb://localhost:27017/')
#         self.db = self.client['BookstoreDB']
#         self.collection = self.db['books']

#     def process_item(self, item, spider):
#         try:
#             self.collection.insert_one(dict(item))
#             return item
#         except Exception as e:
#             raise DropItem(f"Error inserting item: {e}")

class JsonPipeline:
    def __init__(self):
        self.data = []

    def process_item(self, item, spider):
        self.data.append(dict(item))
        return item

    def open_spider(self, spider):
        self.file = open('books.json', 'w', encoding='utf-8')

    def close_spider(self, spider):
        json.dump(self.data, self.file, ensure_ascii=False, indent=4)
        self.file.close()

# class MySQLPipeline:
#     def __init__(self):
#         self.connect = mysql.connector.connect(
#             host='localhost',
#             user='root',
#             password='12345678',
#             database='bookstoredb'
#         )
#         self.cursor = self.connect.cursor()
#         self.cursor.execute("""
#         CREATE TABLE IF NOT EXISTS books(
#             id int NOT NULL auto_increment,
#             tensach text,
#             giagoc text,
#             giagiam text,
#             tacgia text,
#             nguoidich text,
#             kichthuoc text,
#             sotrang text,
#             hinhthuc text,
#             PRIMARY KEY (id)
#         )
#         """)

#     def process_item(self, item, spider):
#         self.cursor.execute('''
#             INSERT INTO books(tensach, giagoc, giagiam, tacgia, nguoidich, kichthuoc, sotrang, hinhthuc)
#             VALUES(%s, %s, %s, %s, %s, %s, %s, %s)''', (
#             item['tensach'],
#             item['giagoc'],
#             item['giagiam'],
#             item['tacgia'],
#             item['nguoidich'],
#             item['kichthuoc'],
#             item['sotrang'],
#             item['hinhthuc']
#         ))
#         self.connect.commit()
#         return item

#     def close_spider(self, spider):
#         self.cursor.close()
#         self.connect.close()

class CSVPipeline:
    def process_item(self, item, spider):
        self.file = open('books.csv', 'a', newline='', encoding='utf-8')
        self.csv_writer = csv.writer(self.file)
        self.csv_writer.writerow([item['tensach'], item['giagoc'], item['giagiam'], item['tacgia'], item['nguoidich'], item['kichthuoc'], item['sotrang'], item['hinhthuc']])
        self.file.close()
        return item

class PostgresPipeline:
    def __init__(self):
        self.connect = psycopg2.connect(
            host='postgres_db',
            user='user',
            password='123',
            database='bookstore'
        )
        self.cursor = self.connect.cursor()
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS books(
            id serial primary key,
            tensach text,
            giagoc text,
            giagiam text,
            tacgia text,
            nguoidich text,
            kichthuoc text,
            sotrang text,
            hinhthuc text
        )
        """)

    def process_item(self, item, spider):
        self.cursor.execute('''INSERT INTO books(tensach, giagoc, giagiam, tacgia, nguoidich, kichthuoc, sotrang, hinhthuc)
            VALUES(%s, %s, %s, %s, %s, %s, %s, %s)''', (
            item['tensach'],
            item['giagoc'],
            item['giagiam'],
            item['tacgia'],
            item['nguoidich'],
            item['kichthuoc'],
            item['sotrang'],
            item['hinhthuc']
        ))
        self.connect.commit()
        print("Cào thành công!!!")
        return item

    def close_spider(self, spider):
        self.connect.close()
        self.cursor.close()