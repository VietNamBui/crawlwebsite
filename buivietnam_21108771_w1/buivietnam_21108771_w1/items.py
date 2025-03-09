# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


# class Buivietnam21108771W1Item(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     pass

class BookItem(scrapy.Item):
    tensach = scrapy.Field()
    giagoc = scrapy.Field()
    giagiam = scrapy.Field()
    tacgia = scrapy.Field()
    nguoidich = scrapy.Field()
    kichthuoc = scrapy.Field()
    sotrang = scrapy.Field()
    hinhthuc = scrapy.Field()
