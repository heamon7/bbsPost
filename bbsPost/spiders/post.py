# -*- coding: utf-8 -*-
import scrapy
from scrapy.shell import inspect_response
from scrapy.http import Request,FormRequest

import re
import logging
from scrapy import log
from scrapy.exceptions import DropItem

from  bbsPost.items import BbspostItem
from bbsPost import settings

import os


class PostSpider(scrapy.Spider):
    name = "post"
    allowed_domains = ["byr.cn"]
    start_urls = (
        'http://bbs.byr.cn/',
    )
    baseUrl = 'http://bbs.byr.cn'
    def __init__(self):
        # self.stats = stats
       pass
    # @classmethod
    # def from_crawler(cls, crawler):
    #     return cls(crawler.stats)

    def start_requests(self):
        #print "start_requests ing ......"
        #print self.urls

        yield FormRequest(url ='http://bbs.byr.cn/user/ajax_login.json',
                          formdata={
                              'id':'NewUser'
                              ,'passwd':'newuser!@#'
                              ,'CookieDate':'2'
                          }
                          ,callback = self.afterLogin)

    def afterLogin(self,response):
        logging.warning(str(response.body))
        yield FormRequest(url = 'http://bbs.byr.cn/article/BUPTNet/ajax_post.json'
                          ,formdata={
                          'content':'bd,美分一顶'
                          ,'id':'75627'
                          ,'subject':'Re: 信息黄埔，互联网+。。。。。。。'
                            }
                          ,callback=self.parse)
    def parse(self, response):
        logging.warning(str(response.body))

        item = BbspostItem()


        return item
    def closed(self,reason):

        pass
