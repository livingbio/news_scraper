# -*- coding: utf-8 -*-
from scrapy import Spider, Request
from scraper_app.models import Article, ArticleItem
from datetime import date, timedelta


class LTN_Spider(Spider):

    name = 'news.ltn.com.tw'
    allowed_domains = ['news.ltn.com.tw']

    def url_type_date(self, typ, dat):
        return 'http://{}/newspaper/{}/{}'. \
               format(self.name, typ, dat.strftime('%Y%m%d'))

    def url_path(self, rel_path):
        return 'http://{}/{}'.format(self.name, rel_path)

    def start_requests(self):
        one_day = timedelta(days=1)
        start_day = date(2014, 10, 1)
        types = ['focus', 'politics', 'society']
        while True:
            for typ in types:
                yield Request(self.url_type_date(typ, start_day), self.parse)
            start_day = start_day + one_day
            if start_day >= date.today():
                break

    def parse(self, response):
        # follow每一個新聞連結
        for path in response.xpath('//ul[@id="newslistul"]//a/@href').extract():
            yield Request(self.url_path(path), self.parse_news)

        # 檢查是否有下一頁
        for page in response.xpath('//strong[@class="p_num"]/following-sibling::a[1]/@href').extract():
            yield Request(self.url_path(page), self.parse)

    def parse_news(self, response):
        text = []
        for paragraph in response.xpath('//div[@id="newstext"]/p/text()').extract():
            text.append(paragraph)

        keywords = []
        for kw in response.xpath('//div[@class="con_keyword boxTitle"]/a/text()').extract():
            keywords.append(keywords)
