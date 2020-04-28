# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Bank(scrapy.Item):
  bank_name = scrapy.Field()
  branch_name = scrapy.Field()
  ifsc_code = scrapy.Field()
  # micr_code = scrapy.Field()
  state = scrapy.Field()
  district = scrapy.Field()
  city = scrapy.Field()
  branch_code = scrapy.Field()
  address = scrapy.Field()
  phone_no = scrapy.Field()
